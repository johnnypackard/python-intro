print("What's brown and sounds like a bell?")
print("Dung!")

from flask import Flask
app = Flask("Johnny")

@app.route("/")
def hello():
    return "Hello World!"

