import os
import io
import time
import base64
import random
import webbrowser
from threading import Timer
from PIL import Image
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

import torchvision.models as models

# ==========================================
# 1. ResNet-50 Model Architecture & Setup
# ==========================================
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
GPU_NAME = torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU'
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'resnet50.pth')
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'flower_photos_test', 'flower_photos_test')

CLASS_METADATA = {
    'daisy': {
        'name_en': 'Daisy',
        'scientific_name': 'Bellis perennis (Asteraceae)',
        'color': '#0ea5e9',
        'description': 'Perennial herbaceous plant featuring clean white ray florets surrounding a vibrant central golden disc.',
    },
    'dandelion': {
        'name_en': 'Dandelion',
        'scientific_name': 'Taraxacum officinale (Asteraceae)',
        'color': '#f59e0b',
        'description': 'Perennial herbaceous plant characterized by bright golden-yellow composite florets and deeply serrated foliage.',
    },
    'roses': {
        'name_en': 'Roses',
        'scientific_name': 'Rosa (Rosaceae)',
        'color': '#f43f5e',
        'description': 'Woody perennial flowering plant renowned for intricate multi-layered petals, thorns, and delicate aromatic fragrance.',
    },
    'sunflowers': {
        'name_en': 'Sunflowers',
        'scientific_name': 'Helianthus annuus (Asteraceae)',
        'color': '#eab308',
        'description': 'Tall annual agricultural and ornamental plant with large circular composite flower heads displaying prominent heliotropism.',
    },
    'tulips': {
        'name_en': 'Tulips',
        'scientific_name': 'Tulipa (Liliaceae)',
        'color': '#8b5cf6',
        'description': 'Bulbous spring-flowering geophyte distinguished by symmetrical, cup-shaped blossoms across vivid, saturated color spectrums.',
    }
}
CLASSES = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

# Standard Preprocessing Pipeline
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Load ResNet-50 Model
model = models.resnet50(weights=None)
model.fc = nn.Sequential(
    nn.Dropout(0.3),
    nn.Linear(model.fc.in_features, 5)
)
model = model.to(DEVICE)

if os.path.exists(MODEL_PATH):
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    print(f"[*] High-accuracy ResNet-50 weights successfully loaded from {MODEL_PATH} on {DEVICE}")
else:
    print(f"[!] Warning: Model file {MODEL_PATH} not found!")

model.eval()

# ==========================================
# 3. API Endpoints
# ==========================================
@app.route('/')
def index():
    return render_template('index.html', gpu_name=GPU_NAME, device=DEVICE)

@app.route('/api/system_info')
def system_info():
    return jsonify({
        'device': DEVICE,
        'gpu_name': GPU_NAME,
        'model_name': 'ResNet-50 (Deep Residual Network)',
        'parameters': '25.5 Million',
        'input_size': '224 x 224 px',
        'classes_count': 5,
        'framework': f'PyTorch {torch.__version__}'
    })

@app.route('/api/samples')
def get_samples():
    """Return a curated list of sample test images for quick testing."""
    samples = []
    if os.path.exists(TEST_DATA_DIR):
        for c in CLASSES:
            c_dir = os.path.join(TEST_DATA_DIR, c)
            if os.path.isdir(c_dir):
                files = [f for f in os.listdir(c_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                if files:
                    chosen_file = files[0]
                    samples.append({
                        'class_key': c,
                        'name_en': CLASS_METADATA[c]['name_en'],
                        'scientific_name': CLASS_METADATA[c]['scientific_name'],
                        'color': CLASS_METADATA[c]['color'],
                        'filename': chosen_file,
                        'url': f'/api/sample_image/{c}/{chosen_file}'
                    })
    return jsonify(samples)

@app.route('/api/sample_image/<class_key>/<filename>')
def serve_sample_image(class_key, filename):
    if class_key in CLASSES:
        dir_path = os.path.join(TEST_DATA_DIR, class_key)
        return send_from_directory(dir_path, filename)
    return "Not found", 404

@app.route('/api/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200
    try:
        t0 = time.perf_counter()
        image = None

        # 1. From uploaded file
        if 'file' in request.files:
            file = request.files['file']
            image = Image.open(file.stream).convert('RGB')
        # 2. From Base64 JSON
        elif request.is_json and 'image_base64' in request.json:
            b64_data = request.json['image_base64']
            if ',' in b64_data:
                b64_data = b64_data.split(',')[1]
            img_bytes = base64.b64decode(b64_data)
            image = Image.open(io.BytesIO(img_bytes)).convert('RGB')
        # 3. From sample path
        elif request.is_json and 'sample_class' in request.json and 'sample_filename' in request.json:
            s_class = request.json['sample_class']
            s_file = request.json['sample_filename']
            sample_path = os.path.join(TEST_DATA_DIR, s_class, s_file)
            if os.path.exists(sample_path):
                image = Image.open(sample_path).convert('RGB')

        if image is None:
            return jsonify({'error': 'No image provided'}), 400

        # Preprocess
        tensor = transform(image).unsqueeze(0).to(DEVICE)

        # Forward pass
        with torch.no_grad():
            outputs = model(tensor)
            probs = torch.softmax(outputs, dim=1)[0].cpu().numpy()

        latency_ms = round((time.perf_counter() - t0) * 1000, 2)

        # Build prediction list
        predictions = []
        for i, class_key in enumerate(CLASSES):
            confidence_pct = round(float(probs[i]) * 100, 2)
            meta = CLASS_METADATA[class_key]
            predictions.append({
                'class_key': class_key,
                'name_en': meta['name_en'],
                'scientific_name': meta['scientific_name'],
                'color': meta['color'],
                'description': meta['description'],
                'confidence': confidence_pct
            })

        # Sort descending by confidence
        predictions.sort(key=lambda x: x['confidence'], reverse=True)
        top_prediction = predictions[0]

        return jsonify({
            'success': True,
            'top_prediction': top_prediction,
            'all_predictions': predictions,
            'latency_ms': latency_ms,
            'device': DEVICE,
            'gpu_name': GPU_NAME
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == '__main__':
    print("=" * 60)
    print(" GullNas • ResNet-50 Flower Classification System")
    print(" Server Endpoint: http://127.0.0.1:5000")
    print(f" Hardware Device: {GPU_NAME} ({DEVICE})")
    print("=" * 60)
    Timer(1.2, open_browser).start()
    app.run(host='0.0.0.0', port=5000, debug=False)
