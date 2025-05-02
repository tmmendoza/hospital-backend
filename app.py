from flask import Flask, request, jsonify
from otp_utils import request_otp, verify_otp

app = Flask(__name__)

SENDER_EMAIL = 'terrencemendoza@gmail.com'
SENDER_PASS = 'npcu wygv pfjn gvpy'  # Use an App Password, not your Gmail password

@app.route('/')
def home():
    return "Hello, Flask API!"

@app.route('/signup', methods=['POST'])
def signup():
    email = request.json['email']
    request_otp(email, SENDER_EMAIL, SENDER_PASS)
    return jsonify({'message': 'OTP sent to email'})

@app.route('/verify', methods=['POST'])
def verify():
    email = request.json['email']
    otp = request.json['otp']
    if verify_otp(email, otp):
        return jsonify({'message': 'Verified!'})
    return jsonify({'message': 'Invalid or expired OTP'}), 400

if __name__ == '__main__':
    app.run(debug=True)
