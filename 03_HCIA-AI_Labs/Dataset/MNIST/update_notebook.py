import json

notebook_path = r'c:\Users\HC\Desktop\HCIA-AI Labs\Dataset\MNIST\HCIA_AI_ResNet50_Flower_Lab.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cfg_cell_code = """cfg = edict({
    'data_path': './flower_photos_train/flower_photos_train', # Path to training dataset
    'test_path': './flower_photos_test/flower_photos_test',   # Path to test dataset
    'data_size': 3616,
    'HEIGHT': 224,                              # Image height
    'WIDTH': 224,                               # Image width
    '_R_MEAN': 123.68,                          # Mean color normalization values
    '_G_MEAN': 116.78,
    '_B_MEAN': 103.94,
    '_R_STD': 1.0,                              # Standard deviation value
    '_G_STD': 1.0,
    '_B_STD': 1.0,
    '_RESIZE_SIDE_MIN': 256,
    '_RESIZE_SIDE_MAX': 512,
    'batch_size': 16,                           # Batch size (optimized for GPU)
    'num_class': 5,                             # Number of flower classes
    'epoch_size': 5,                            # Number of training epochs
    'num_workers': 0,                           # Number of workers
    'device': 'cuda' if torch.cuda.is_available() else 'cpu', # Compute device (GPU / CPU)
    'prefix': 'resnet50.pth',                   # Model checkpoint output filename
})"""

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source_str = ''.join(cell['source'])
        if 'cfg = edict' in source_str:
            cell['source'] = [line + '\n' for line in cfg_cell_code.split('\n')]
            cell['outputs'] = []
            cell['execution_count'] = None

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Notebook updated with batch_size 16')
