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
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Helper function to safely parse input
        def parse_input(value):
            value = value.strip().replace(',', '')  # Remove commas
            return float(value)

        features = [
    parse_input(request.form['price']),
    parse_input(request.form['24h']),
    parse_input(request.form['24h_volume']),
    parse_input(request.form['mkt_cap'])
]


        prediction = model.predict([features])[0]
        return render_template('index.html', prediction_text=f"📈 Predicted Liquidity: {prediction:.2f}")

    except ValueError:
        return render_template('index.html', prediction_text="⚠️ Please enter valid numeric values for all fields.")
    except Exception as e:
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
