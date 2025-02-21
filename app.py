from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from PIL import Image
import torch
from torchvision import transforms
from huggingface_hub import login

app = Flask(__name__)

model = pipeline("image-classification", model="umm-maybe/AI-image-detector")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected image'}), 400

    img = Image.open(file)
    
    preprocess = transforms.Compose([
        transforms.ToTensor()
    ])

    img_tensor = preprocess(img).unsqueeze(0)

    result = model(img)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
