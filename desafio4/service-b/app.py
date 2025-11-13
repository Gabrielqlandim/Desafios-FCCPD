import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# URL do serviço de usuários (Microsserviço A)
# Em Docker, vamos passar algo tipo: http://service-a:5000/users
USERS_API_URL = os.getenv("USERS_API_URL", "http://localhost:5001/users")

@app.route("/report", methods=["GET"])
def report():
    try:
        resp = requests.get(USERS_API_URL, timeout=3)
        resp.raise_for_status()
        users = resp.json()
    except Exception as e:
        return jsonify({
            "error": "Erro ao chamar serviço de usuários",
            "details": str(e),
            "users_api_url": USERS_API_URL
        }), 502

    messages = [
        f"Usuário {u.get('name')} ativo desde {u.get('active_since')}"
        for u in users
    ]

    return jsonify({
        "source": USERS_API_URL,
        "total_users": len(users),
        "messages": messages
    })

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # Porta interna 5000
    app.run(host="0.0.0.0", port=5000)
