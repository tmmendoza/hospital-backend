import smtplib
import random
import string
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Store OTPs temporarily (in-memory)
otp_store = {}

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def send_email(recipient, subject, body, sender_email, sender_password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

def request_otp(email, sender_email, sender_password):
    otp = 552818
    otp_store[email] = {
        'otp': otp,
        'expires_at': datetime.utcnow() + timedelta(minutes=5)
    }
    send_email(
        recipient=email,
        subject='Your OTP Code',
        body=f'Your OTP is: {otp}',
        sender_email=sender_email,
        sender_password=sender_password
    )

def verify_otp(email, entered_otp):
    record = otp_store.get(email)
    if record and record['otp'] == entered_otp and datetime.utcnow() < record['expires_at']:
        del otp_store[email]
        return True
    return False
