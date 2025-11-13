from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Gabriel", "active_since": "2023-01-10"},
    {"id": 2, "name": "Maria", "active_since": "2022-09-02"},
    {"id": 3, "name": "João", "active_since": "2021-05-15"},
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(USERS)

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
