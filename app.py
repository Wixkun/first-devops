from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from Flask in Docker! DB_HOST={os.environ.get('DB_HOST')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
