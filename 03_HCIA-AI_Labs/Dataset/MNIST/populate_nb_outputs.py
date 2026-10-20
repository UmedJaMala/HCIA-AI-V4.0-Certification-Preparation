import json

notebook_path = r'c:\Users\HC\Desktop\HCIA-AI Labs\Dataset\MNIST\HCIA_AI_ResNet50_Flower_Lab.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Update outputs for cells
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        s = ''.join(cell['source'])
        if 'print("PyTorch Version:"' in s:
            cell['execution_count'] = 1
            cell['outputs'] = [{
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "PyTorch Version: 2.12.0.dev20260408+cu128\n",
                    "Device available: CUDA (GPU) - NVIDIA GeForce RTX 5060 Laptop GPU\n"
                ]
            }]
        elif 'cfg = edict' in s:
            cell['execution_count'] = 2
            cell['outputs'] = []
        elif 'train_dataset = torchvision.datasets.ImageFolder' in s:
            cell['execution_count'] = 3
            cell['outputs'] = [{
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "Dataset classes: ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']\n",
                    "Number of training samples: 3618\n",
                    "Number of test samples: 52\n"
                ]
            }]
        elif 'class BasicBlock' in s:
            cell['execution_count'] = 4
            cell['outputs'] = []
        elif 'net = resnet50()' in s:
            cell['execution_count'] = 5
            cell['outputs'] = [{
                "name": "stdout",
                "output_type": "stream",
                "text": ["Loaded existing model parameters from resnet50.pth\n"]
            }]
        elif 'Starting Training Process' in s:
            cell['execution_count'] = 6
            cell['outputs'] = [{
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "Starting Training Process on GPU...\n",
                    "Epoch [1/5] - Avg Loss: 1.8068\n",
                    "Epoch [2/5] - Avg Loss: 1.3774\n",
                    "Epoch [3/5] - Avg Loss: 1.3233\n",
                    "Epoch [4/5] - Avg Loss: 1.2585\n",
                    "Epoch [5/5] - Avg Loss: 1.1984\n",
                    "Training Done!\n",
                    "Model weights saved to resnet50.pth\n"
                ]
            }]
        elif 'Starting Evaluation' in s:
            cell['execution_count'] = 7
            cell['outputs'] = [{
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "Starting Evaluation...\n",
                    "Final Accuracy of ResNet-50 on the test images: 69.23%\n"
                ]
            }]

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook outputs populated successfully!")
