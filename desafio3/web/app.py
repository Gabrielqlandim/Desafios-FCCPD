import os
from flask import Flask, jsonify
import psycopg2
import redis

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "desafio3db")
DB_USER = os.getenv("DB_USER", "usuario")
DB_PASSWORD = os.getenv("DB_PASSWORD", "senha123")

REDIS_HOST = os.getenv("REDIS_HOST", "cache")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

def test_postgres():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.fetchone()
        cur.close()
        conn.close()
        return True, "Conexão com Postgres OK"
    except Exception as e:
        return False, f"Erro ao conectar no Postgres: {e}"

def test_redis():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        r.set("teste", "ok")
        value = r.get("teste")
        return True, f"Conexão com Redis OK (valor={value.decode()})"
    except Exception as e:
        return False, f"Erro ao conectar no Redis: {e}"

@app.route("/")
def healthcheck():
    pg_ok, pg_msg = test_postgres()
    rd_ok, rd_msg = test_redis()

    status = 200 if (pg_ok and rd_ok) else 500

    return jsonify({
        "mensagem": "Desafio 3 - Docker Compose Orquestrando Serviços",
        "postgres": pg_msg,
        "redis": rd_msg
    }), status
