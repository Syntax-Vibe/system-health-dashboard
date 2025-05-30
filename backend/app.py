from flask import Flask, jsonify
import psutil
import datetime

app = Flask(__name__)

@app.route('/health')
def health():
    data = {
        'cpu': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent,
        'time': datetime.datetime.now().strftime('%H:%M:%S')
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
