from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')  # Simple test route
def home():
    return "Flask is running!"

@app.route('/check_fact', methods=['POST'])
def check_fact():
    data = request.get_json()
    return jsonify({"received": data})

#if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Allow external access if needed
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)  # Change to 5001
