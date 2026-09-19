"""
Run this to generate certificate
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HTTPS Enabled!"

app.run(host="0.0.0.0", port=443,
        ssl_context=("cert.pem", "key.pem"))