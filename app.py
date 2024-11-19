from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Loading model and scaler
model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_anomaly', methods=['POST'])
def check_anomaly():
    data = request.json
    features = np.array([[data['requests_per_minute'], data['response_time']]])
    scaled_features = scaler.transform(features)
    
    # Unusual Predictions
    result = model.predict(scaled_features)
    response = 'Anomaly' if result[0] == -1 else 'Normal'
    
    return jsonify({'status': response})

if __name__ == '__main__':
    app.run(debug=True)
