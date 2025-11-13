from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "message": "Olá, eu sou o servidor web do Desafio 1 😄",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "host": socket.gethostname()
    }

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=8080)
