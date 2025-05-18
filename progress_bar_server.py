from flask import Flask, request, Response
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

@app.route("/progress")
def progress_svg():
    # Parameters
    value = int(request.args.get("value", 0))
    theme = request.args.get("theme", "light").lower()

    # Clamp value
    value = max(0, min(100, value))

    # Appearance
    bar_height = 5
    text_padding = 10
    total_width = 400
    bar_width = 300  # width of the bar portion only

    # Colors
    if theme == "dark":
        bg_color = "#000000"
        text_color = "#FFFFFF"
        bar_bg_color = "#5A5A5A"
    else:
        bg_color = "#FFFFFF"
        text_color = "#000000"
        bar_bg_color = "#DADADA"

    bar_fill_color = "#00C800"  # green
    progress_width = int(bar_width * value / 100)

    # SVG content
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg width="{total_width}" height="30" xmlns="http://www.w3.org/2000/svg">
  <rect width="{total_width}" height="30" fill="{bg_color}" />
  <g transform="translate(20,12)">
    <rect rx="{bar_height/2}" ry="{bar_height/2}" width="{bar_width}" height="{bar_height}" fill="{bar_bg_color}" />
    <rect rx="{bar_height/2}" ry="{bar_height/2}" width="{progress_width}" height="{bar_height}" fill="{bar_fill_color}" />
  </g>
  <text x="{20 + bar_width + 10}" y="20" font-family="monospace" font-size="14" fill="{text_color}">{value}%</text>
</svg>
"""
    return Response(svg, mimetype="image/svg+xml")
