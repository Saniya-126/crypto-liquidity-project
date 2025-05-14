from flask import Flask, request, render_template
import joblib
import os
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load(os.path.join(os.path.dirname(__file__), "linear_regression_model.pkl"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form values in order
        features = [
            float(request.form['price']),
            float(request.form['1h']),
            float(request.form['24h']),
            float(request.form['7d']),
            float(request.form['24h_volume']),
            float(request.form['mkt_cap'])
        ]

        prediction = model.predict([features])[0]
        return render_template('index.html', prediction_text=f"📈 Predicted Liquidity: {prediction:.2f}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
