import os
import time
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from easydict import EasyDict as edict
from torch.utils.data import TensorDataset, DataLoader

def main():
    print("=== Super Fast GPU Training for HCIA-AI ResNet-50 ===")
    t_start = time.time()

    cfg = edict({
        'data_path': './flower_photos_train/flower_photos_train',
        'test_path': './flower_photos_test/flower_photos_test',
        'HEIGHT': 224,
        'WIDTH': 224,
        '_R_MEAN': 123.68,
        '_G_MEAN': 116.78,
        '_B_MEAN': 103.94,
        '_R_STD': 1.0,
        '_G_STD': 1.0,
        '_B_STD': 1.0,
        '_RESIZE_SIDE_MIN': 256,
        'batch_size': 8, # Fits comfortably in 8GB VRAM with large 224x224 feature maps
        'num_class': 5,
        'epoch_size': 5,
        'device': 'cuda' if torch.cuda.is_available() else 'cpu',
        'prefix': 'resnet50.pth',
    })

    print(f"Device: {cfg.device} ({torch.cuda.get_device_name(0)})")

    # Fast preprocessing
    transform_train = transforms.Compose([
        transforms.Resize((cfg.HEIGHT, cfg.WIDTH)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[cfg._R_MEAN/255.0, cfg._G_MEAN/255.0, cfg._B_MEAN/255.0], std=[cfg._R_STD/255.0, cfg._G_STD/255.0, cfg._B_STD/255.0]),
    ])

    transform_test = transforms.Compose([
        transforms.Resize((cfg.HEIGHT, cfg.WIDTH)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[cfg._R_MEAN/255.0, cfg._G_MEAN/255.0, cfg._B_MEAN/255.0], std=[cfg._R_STD/255.0, cfg._G_STD/255.0, cfg._B_STD/255.0]),
    ])

    print("Pre-loading images into fast memory cache...")
    raw_train = torchvision.datasets.ImageFolder(cfg.data_path, transform=transform_train)
    raw_test = torchvision.datasets.ImageFolder(cfg.test_path, transform=transform_test)

    train_imgs = []
    train_lbls = []
    for img, lbl in raw_train:
        train_imgs.append(img)
        train_lbls.append(lbl)
    
    train_imgs = torch.stack(train_imgs)
    train_lbls = torch.tensor(train_lbls)
    
    train_dataset = TensorDataset(train_imgs, train_lbls)
    trainloader = DataLoader(train_dataset, batch_size=cfg.batch_size, shuffle=True)

    test_imgs = []
    test_lbls = []
    for img, lbl in raw_test:
        test_imgs.append(img)
        test_lbls.append(lbl)
    
    test_imgs = torch.stack(test_imgs)
    test_lbls = torch.tensor(test_lbls)
    
    test_dataset = TensorDataset(test_imgs, test_lbls)
    testloader = DataLoader(test_dataset, batch_size=cfg.batch_size, shuffle=False)

    print(f"Loaded {len(train_dataset)} training images and {len(test_dataset)} test images.")
    print(f"Pre-loading time: {time.time() - t_start:.2f}s")

    # ResNet-50 Definition matching the Lab
    class BottleNeck(nn.Module):
        expansion = 4
        def __init__(self, in_channels, out_channels, stride=1):
            super(BottleNeck, self).__init__()
            self.residual_function = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, bias=False),
                nn.BatchNorm2d(out_channels),
                nn.ReLU(inplace=True),
                nn.Conv2d(out_channels, out_channels, stride=stride, kernel_size=3, padding=1, bias=False),
                nn.BatchNorm2d(out_channels),
                nn.ReLU(inplace=True),
                nn.Conv2d(out_channels, out_channels * BottleNeck.expansion, kernel_size=1, bias=False),
                nn.BatchNorm2d(out_channels * BottleNeck.expansion)
            )
            self.shortcut = nn.Sequential()
            if stride != 1 or in_channels != out_channels * BottleNeck.expansion:
                self.shortcut = nn.Sequential(
                    nn.Conv2d(in_channels, out_channels * BottleNeck.expansion, stride=stride, kernel_size=1, bias=False),
                    nn.BatchNorm2d(out_channels * BottleNeck.expansion)
                )
        def forward(self, x):
            return nn.ReLU(inplace=True)(self.residual_function(x) + self.shortcut(x))

    class ResNet(nn.Module):
        def __init__(self, block, num_block, num_classes=5):
            super(ResNet, self).__init__()
            self.in_channels = 64
            self.conv1 = nn.Sequential(
                nn.Conv2d(3, 64, kernel_size=3, padding=1, bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(inplace=True)
            )
            self.conv2_x = self._make_layer(block, 64, num_block[0], 1)
            self.conv3_x = self._make_layer(block, 128, num_block[1], 2)
            self.conv4_x = self._make_layer(block, 256, num_block[2], 2)
            self.conv5_x = self._make_layer(block, 512, num_block[3], 2)
            self.avg_pool = nn.AdaptiveAvgPool2d((1, 1))
            self.fc = nn.Linear(512 * block.expansion, num_classes)

        def _make_layer(self, block, out_channels, num_blocks, stride):
            strides = [stride] + [1] * (num_blocks - 1)
            layers = []
            for stride in strides:
                layers.append(block(self.in_channels, out_channels, stride))
                self.in_channels = out_channels * block.expansion
            return nn.Sequential(*layers)

        def forward(self, x):
            out = self.conv1(x)
            out = self.conv2_x(out)
            out = self.conv3_x(out)
            out = self.conv4_x(out)
            out = self.conv5_x(out)
            out = self.avg_pool(out)
            out = out.view(out.size(0), -1)
            out = self.fc(out)
            return out

    net = ResNet(BottleNeck, [3, 4, 6, 3], num_classes=cfg.num_class).to(cfg.device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9, weight_decay=0.0001)
    scaler = torch.amp.GradScaler('cuda')

    print("\nStarting Training on RTX 5060 GPU...")
    t_train_start = time.time()
    net.train()

    for epoch in range(cfg.epoch_size):
        t_epoch_start = time.time()
        running_loss = 0.0
        losses = []
        for i, (inputs, labels) in enumerate(trainloader):
            inputs = inputs.to(cfg.device, non_blocking=True)
            labels = labels.to(cfg.device, non_blocking=True)

            optimizer.zero_grad()
            with torch.amp.autocast('cuda'):
                outputs = net(inputs)
                loss = criterion(outputs, labels)
            
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()

            losses.append(loss.item())
            running_loss += loss.item()

        avg_loss = sum(losses) / len(losses)
        epoch_time = time.time() - t_epoch_start
        print(f"Epoch [{epoch+1}/{cfg.epoch_size}] - Avg Loss: {avg_loss:.4f} - Time: {epoch_time:.2f}s", flush=True)

    total_train_time = time.time() - t_train_start
    print(f"\nTraining Complete! Total GPU Training Time: {total_train_time:.2f} seconds", flush=True)

    torch.save(net.state_dict(), cfg.prefix)
    print(f"Model saved to {cfg.prefix}", flush=True)

    print("\nEvaluating on Test Set...", flush=True)
    net.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in testloader:
            inputs, labels = inputs.to(cfg.device), labels.to(cfg.device)
            with torch.amp.autocast('cuda'):
                outputs = net(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    acc = 100.0 * correct / total
    print(f"Final Test Accuracy: {acc:.2f}%", flush=True)
    print(f"Total Overall Time: {time.time() - t_start:.2f} seconds", flush=True)

if __name__ == '__main__':
    main()
