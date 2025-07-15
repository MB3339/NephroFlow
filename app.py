from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
import base64
from cnnClassifier.pipeline.prediction import PredictionPipeline
from cnnClassifier.utils.common import decodeImage

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        data = request.get_json()
        image_data = data.get('image')

        # Decode the base64 image
        image_path = os.path.join(UPLOAD_FOLDER, "input_image.png")
        decodeImage(image_data, image_path)

        # Run prediction
        prediction_pipeline = PredictionPipeline(filename=image_path)
        result = prediction_pipeline.predict()

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
