import os
import random
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from easydict import EasyDict as edict

# 1. Configuration
cfg = edict({
    'data_path': './flower_photos_train/flower_photos_train',
    'test_path': './flower_photos_test/flower_photos_test',
    'data_size': 3616,
    'HEIGHT': 224,
    'WIDTH': 224,
    '_R_MEAN': 123.68,
    '_G_MEAN': 116.78,
    '_B_MEAN': 103.94,
    '_R_STD': 1.0,
    '_G_STD': 1.0,
    '_B_STD': 1.0,
    '_RESIZE_SIDE_MIN': 256,
    '_RESIZE_SIDE_MAX': 512,
    'batch_size': 16, # Optimized batch size for 8GB VRAM
    'num_class': 5,
    'epoch_size': 5,
    'num_workers': 0,
    'device': 'cuda' if torch.cuda.is_available() else 'cpu',
    'prefix': 'resnet50.pth',
})

print(f"Device in use: {cfg.device} ({torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU'})")

# 2. Transforms & DataLoaders
transform_train = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(mean=[cfg._R_MEAN, cfg._G_MEAN, cfg._B_MEAN], std=[cfg._R_STD, cfg._G_STD, cfg._B_STD]),
    transforms.Resize(cfg._RESIZE_SIDE_MIN),
    transforms.CenterCrop((cfg.HEIGHT, cfg.WIDTH)),
])

transform_test = transforms.Compose([
    transforms.Resize(cfg._RESIZE_SIDE_MIN),
    transforms.CenterCrop((cfg.HEIGHT, cfg.WIDTH)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[cfg._R_MEAN, cfg._G_MEAN, cfg._B_MEAN], std=[cfg._R_STD, cfg._G_STD, cfg._B_STD]),
])

train_dataset = torchvision.datasets.ImageFolder(cfg.data_path, transform=transform_train)
trainloader = torch.utils.data.DataLoader(train_dataset, batch_size=cfg.batch_size, shuffle=True, num_workers=cfg.num_workers)

test_dataset = torchvision.datasets.ImageFolder(cfg.test_path, transform=transform_test)
testloader = torch.utils.data.DataLoader(test_dataset, batch_size=cfg.batch_size, shuffle=False, num_workers=cfg.num_workers)

print(f"Dataset classes: {train_dataset.classes}")
print(f"Number of training samples: {len(train_dataset)}")
print(f"Number of test samples: {len(test_dataset)}")

# 3. ResNet-50 Definition
class BasicBlock(nn.Module):
    expansion = 1
    def __init__(self, in_channels, out_channels, stride=1):
        super(BasicBlock, self).__init__()
        self.residual_function = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels * BasicBlock.expansion, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels * BasicBlock.expansion)
        )
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != BasicBlock.expansion * out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels * BasicBlock.expansion, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels * BasicBlock.expansion)
            )
    def forward(self, x):
        return nn.ReLU(inplace=True)(self.residual_function(x) + self.shortcut(x))

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
    def __init__(self, block, num_block, num_classes=100):
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
        output = self.conv1(x)
        output = self.conv2_x(output)
        output = self.conv3_x(output)
        output = self.conv4_x(output)
        output = self.conv5_x(output)
        output = self.avg_pool(output)
        output = output.view(output.size(0), -1)
        output = self.fc(output)
        return output

def resnet50():
    return ResNet(BottleNeck, [3, 4, 6, 3], num_classes=cfg.num_class)

# 4. Model, Loss, Optimizer
net = resnet50().to(cfg.device)

if os.path.isfile(cfg.prefix):
    try:
        net.load_state_dict(torch.load(cfg.prefix, map_location=cfg.device))
        print(f"Loaded existing model parameters from {cfg.prefix}")
    except Exception:
        print("Starting with fresh model weights.")

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.1, momentum=0.9, weight_decay=0.0001)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, factor=0.1, patience=5)

# 5. Training Loop
print("Starting Training Process on GPU...")
net.train()

for epoch in range(cfg.epoch_size):
    losses = []
    running_loss = 0.0
    for i, inp in enumerate(trainloader):
        inputs, labels = inp
        inputs, labels = inputs.to(cfg.device), labels.to(cfg.device)

        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        losses.append(loss.item())
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 30 == 0 and i > 0:
            print(f'Epoch [{epoch+1}/{cfg.epoch_size}], Step [{i}/{len(trainloader)}], Loss: {running_loss / 30:.4f}', flush=True)
            running_loss = 0.0

    avg_loss = sum(losses) / len(losses)
    scheduler.step(avg_loss)
    print(f'--- Epoch [{epoch+1}/{cfg.epoch_size}] Done. Avg Loss: {avg_loss:.4f} ---', flush=True)

print('Training Done!')
torch.save(net.state_dict(), cfg.prefix)
print(f"Model weights saved to {cfg.prefix}")

# 6. Evaluation
print("Starting Evaluation on Test Set...")
net.eval()
correct = 0
total = 0

with torch.no_grad():
    for data in testloader:
        images, labels = data
        images, labels = images.to(cfg.device), labels.to(cfg.device)
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * (correct / total)
print(f'Final Accuracy of ResNet-50 on the test images: {accuracy:.2f}%')
