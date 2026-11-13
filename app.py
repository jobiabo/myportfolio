from flask import Flask, render_template
from waitress import serve

app = Flask(__name__, static_folder='assets', static_url_path='/assets')
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)