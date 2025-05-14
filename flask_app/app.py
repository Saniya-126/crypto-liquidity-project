from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
model_path = os.path.join(os.path.dirname(__file__), "linear_regression_model.pkl")
model = joblib.load(model_path)


app = Flask(__name__)



@app.route('/')
def home():
    return "Crypto Liquidity Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Expected input: dictionary with 4 features
    try:
        price = float(data['price'])
        price_ma7 = float(data['price_ma7'])
        price_volatility = float(data['price_volatility'])
        liquidity_ratio = float(data['liquidity_ratio'])
    except KeyError as e:
        return jsonify({'error': f'Missing input: {str(e)}'}), 400

    features = np.array([[price, price_ma7, price_volatility, liquidity_ratio]])
    prediction = model.predict(features)

    return jsonify({
        'predicted_24h_volume': prediction[0]
    })

if __name__ == '__main__':

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

