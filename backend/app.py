from flask import Flask, jsonify, send_from_directory
import psutil
from datetime import datetime
import os

app = Flask(__name__, static_folder='frontend')

@app.route('/health')
def health():
    return jsonify({
        "cpu": f"{psutil.cpu_percent()}%",
        "disk": f"{psutil.disk_usage('/').percent}%",
        "memory": f"{psutil.virtual_memory().percent}%",
        "time": datetime.now().strftime("%H:%M:%S")
    })

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')
