from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    return f"Cleaning pipelines"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
