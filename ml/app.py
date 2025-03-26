
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
