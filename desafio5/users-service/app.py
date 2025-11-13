from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Gabriel", "email": "gabriel@example.com"},
    {"id": 2, "name": "Maria", "email": "maria@example.com"},
    {"id": 3, "name": "João", "email": "joao@example.com"},
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(USERS)

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok", "service": "users-service"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
