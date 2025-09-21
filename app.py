from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__, template_folder="templates")  # point to templates folder
CORS(app)

MODEL_PATH = 'rainwater_model.pkl'
model = None

def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        try:
            model = joblib.load(MODEL_PATH)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
    else:
        print(f"Error: Model file not found at '{MODEL_PATH}'.")

# --- Serve index.html ---
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# --- API Endpoint for Prediction ---
@app.route("/", methods=["POST"])
def predict():
    if model is None:
        return jsonify({'error': 'Model is not loaded. Check server logs.'}), 500

    try:
        data = request.get_json()

        current_level = data['current_tank_level']
        usage = data['water_usage']
        forecast = data['rainfall_forecast']

        features = np.array([[current_level, usage, forecast]])
        prediction = model.predict(features)

        return jsonify({'predicted_level': round(float(prediction[0]), 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    load_model()
    app.run(debug=True)
