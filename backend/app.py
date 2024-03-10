from flask import Flask
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

@app.route('/api/time', methods=['GET'])
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"The current time is: {current_time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
