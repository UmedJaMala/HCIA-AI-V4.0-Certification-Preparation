import json

notebook_path = r'c:\Users\HC\Desktop\HCIA-AI Labs\Dataset\MNIST\HCIA_AI_ResNet50_Flower_Lab.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cfg_cell_code = """cfg = edict({
    'data_path': './flower_photos_train/flower_photos_train', # ڕاڕەوی داتای مەشقپێکردن
    'test_path': './flower_photos_test/flower_photos_test',   # ڕاڕەوی داتای تاقیکردنەوە
    'data_size': 3616,
    'HEIGHT': 224,                              # بەرزی وێنە
    'WIDTH': 224,                               # پانی وێنە
    '_R_MEAN': 123.68,                          # بەهاکانی ناوەند بۆ ڕەنگەکان
    '_G_MEAN': 116.78,
    '_B_MEAN': 103.94,
    '_R_STD': 1.0,                              # بەهای لادانی پێوانەیی
    '_G_STD': 1.0,
    '_B_STD': 1.0,
    '_RESIZE_SIDE_MIN': 256,
    '_RESIZE_SIDE_MAX': 512,
    'batch_size': 16,                           # قەبارەی باچ (گونجێنراو بۆ GPU)
    'num_class': 5,                             # ژمارەی پۆلەکانی گوڵ
    'epoch_size': 5,                            # ژمارەی خولەکانی ڕاهێنان
    'num_workers': 0,                           # ژمارەی worker
    'device': 'cuda' if torch.cuda.is_available() else 'cpu', # کارکردن لەسەر GPU (NVIDIA RTX 5060)
    'prefix': 'resnet50.pth',                   # ناوی فایلی پاشەکەوتکردنی مۆدێلەکە
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
