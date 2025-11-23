from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def index():
    return jsonify({"message": "Hello from CI sample app"})

def add(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
