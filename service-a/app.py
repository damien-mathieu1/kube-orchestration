from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

SERVICE_B_URL = os.environ.get("SERVICE_B_URL", "http://localhost:8081")


@app.route('/health')
def health():
    try:
        response = requests.get(f'{SERVICE_B_URL}/hello')
        if response.status_code == 200:
            return jsonify(message="Hello from service-a", service_b_response=response.json())
        else:
            return jsonify(message="Hello from service-a", service_b_status="unavailable"), 500
    except requests.exceptions.RequestException as e:
        return jsonify(message="Hello from service-a", service_b_error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
