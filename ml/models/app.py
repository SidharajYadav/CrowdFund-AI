# from flask import Flask, request, jsonify
# import pickle
# import pandas as pd

# # Load the trained model
# model_path = "models/campaign_success_model.pkl"
# with open(model_path, "rb") as file:
#     model = pickle.load(file)

# app = Flask(__name__)

# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()  # Expect JSON payload with feature values
#     features = pd.DataFrame([data["features"]])
#     prediction = model.predict(features)
#     response = {
#         "prediction": int(prediction[0])  # Assuming binary classification (0 or 1)
#     }
#     return jsonify(response)

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
 
 
from flask import Flask, request, jsonify
from joblib import load 
import numpy as np

app = Flask(__name__)

# Load your trained model
model = load("models/campaign_success_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
