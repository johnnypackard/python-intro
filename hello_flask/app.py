from flask import Flask
app = Flask("johnny")

@app.route("/")
def home():
    return 'Hello, Flask!'