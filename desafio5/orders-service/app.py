from flask import Flask, jsonify

app = Flask(__name__)

ORDERS = [
    {"id": 101, "user_id": 1, "item": "Livro de Docker", "total": 79.90},
    {"id": 102, "user_id": 2, "item": "Teclado Mecânico", "total": 350.00},
    {"id": 103, "user_id": 1, "item": "Mouse", "total": 120.00},
]

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(ORDERS)

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok", "service": "orders-service"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
