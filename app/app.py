import os
import socket
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Platform Engineering Capstone</title>
    <style>
        body {
            background-color: {{ color }};
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }
        .card {
            background: rgba(0, 0, 0, 0.45);
            padding: 2.5rem 3.5rem;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.25);
        }
        code {
            background: rgba(255,255,255,0.15);
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>{{ message }}</h1>
        <p>Served by Host / Pod: <code>{{ hostname }}</code></p>
        <p>Active Theme Color: <code>{{ color }}</code></p>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    color = os.getenv("APP_COLOR", "#1e3a8a")
    message = os.getenv("APP_MESSAGE", "Vanilla Platform Engineering Lab")
    hostname = socket.gethostname()
    return render_template_string(HTML_TEMPLATE, color=color, message=message, hostname=hostname)

@app.route("/healthz")
def healthz():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
