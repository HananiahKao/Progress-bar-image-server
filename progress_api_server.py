from flask import Flask, request, send_file
from io import BytesIO
from html_to_image import html_to_png
from requests import get

app = Flask(__name__)

@app.route("/")
def root():
    print("wecome Home!")
    return "", 200
@app.route("/health-check")
def health():
    print("I am still alive!")
    get('https://progerss-bar-provider.onrender.com')
    return "", 200


@app.route("/progress-image")
def progress_image():
    is_dark_mode = (request.args.get("dark") == "true")
    percentage = int(request.args.get("percent", 100))
    html_to_png(percentage, is_dark_mode)

    with open("progress.png", "rb") as fh:
        buffer = BytesIO(fh.read())

    return send_file(buffer, mimetype="image/png")

if __name__ == "__main__":
    app.run(port=10000)
