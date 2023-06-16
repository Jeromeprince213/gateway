from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Initialize CORS
REGISTRATION_SERVICE_URL = 'http://localhost:5001'
LOGIN_SERVICE_URL = 'http://localhost:5002'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response = requests.post(f'{REGISTRATION_SERVICE_URL}/register', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    response = requests.post(f'{LOGIN_SERVICE_URL}/login', json=data)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True,port=5000)
