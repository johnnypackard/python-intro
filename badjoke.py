print("What's brown and sounds like a bell?")
print("Dung!")

from flask import Flask
app = Flask(_name_)

@app.route("/")
def hello():
    return "Hello World!"

