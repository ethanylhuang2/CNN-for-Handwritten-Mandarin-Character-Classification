from flask import Flask, request, jsonify
import pandas as pd
from PIL import Image
import tensorflow as tf
import keras
from keras.models import load_model
import io
import numpy as np
import pickle

app = Flask(__name__)

model = load_model('trained_models/mandarin_classification_v2.keras')

@app.route("/predict", methods=["POST"])

def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'no file part'}), 400
    file = request.files['file']
    image = keras.load_img(io.BytesIO(file.read()), target_size=(56, 56))
    img_array = keras.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)
    img_array = tf.image.rgb_to_grayscale(img_array)
    img_array = img_array / 255.0
    
    prediction = model.predict(img_array)
    predicted_class = np.argumax(prediction, axis=-1)

    def load_dict(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    
    class_names = load_dict('class_names.pkl')
    predicted_class_name = class_names[predicted_class[0]]

    return jsonify({'prediction': predicted_class_name})

if __name__ == '__main__':
    app.run(debug=True)
