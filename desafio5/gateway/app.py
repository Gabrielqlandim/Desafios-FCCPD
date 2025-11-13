import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

USERS_SERVICE_URL = os.getenv("USERS_SERVICE_URL", "http://users-service:5000")
ORDERS_SERVICE_URL = os.getenv("ORDERS_SERVICE_URL", "http://orders-service:5000")

def fetch_json(base_url: str, path: str):
    url = f"{base_url}{path}"
    resp = requests.get(url, timeout=3)
    resp.raise_for_status()
    return resp.json()

@app.route("/users", methods=["GET"])
def gateway_users():
    try:
        users = fetch_json(USERS_SERVICE_URL, "/users")
        return jsonify({
            "via": "gateway",
            "upstream": USERS_SERVICE_URL + "/users",
            "total_users": len(users),
            "data": users
        })
    except Exception as e:
        return jsonify({
            "error": "Erro ao consultar serviço de usuários",
            "details": str(e),
            "upstream": USERS_SERVICE_URL
        }), 502

@app.route("/orders", methods=["GET"])
def gateway_orders():
    try:
        orders = fetch_json(ORDERS_SERVICE_URL, "/orders")
        return jsonify({
            "via": "gateway",
            "upstream": ORDERS_SERVICE_URL + "/orders",
            "total_orders": len(orders),
            "data": orders
        })
    except Exception as e:
        return jsonify({
            "error": "Erro ao consultar serviço de pedidos",
            "details": str(e),
            "upstream": ORDERS_SERVICE_URL
        }), 502

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok", "service": "api-gateway"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
