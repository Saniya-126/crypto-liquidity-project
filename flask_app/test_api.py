import requests

url = "http://127.0.0.1:5000/predict"

payload = {
    "price": 0.45,
    "price_ma7": 0.44,
    "price_volatility": 0.02,
    "liquidity_ratio": 1.15
}

response = requests.post(url, json=payload)
print(response.json())
