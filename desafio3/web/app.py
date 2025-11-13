import os
from flask import Flask, jsonify
from datetime import datetime
import psycopg2
import redis

app = Flask(__name__)


DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "desafio3db")
DB_USER = os.getenv("DB_USER", "usuario")
DB_PASSWORD = os.getenv("DB_PASSWORD", "senha123")


REDIS_HOST = os.getenv("REDIS_HOST", "cache")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )

def get_redis_client():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route("/")
def index():
    info = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "db_status": "unknown",
        "redis_status": "unknown",
        "total_registros_db": None,
        "visitas_redis": None,
    }

    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visitas (
                id SERIAL PRIMARY KEY,
                criado_em TIMESTAMPTZ DEFAULT NOW()
            );
        """)
        conn.commit()

        
        cur.execute("INSERT INTO visitas DEFAULT VALUES;")
        conn.commit()

        
        cur.execute("SELECT COUNT(*) FROM visitas;")
        total = cur.fetchone()[0]

        info["db_status"] = "ok"
        info["total_registros_db"] = total

        cur.close()
        conn.close()
    except Exception as e:
        info["db_status"] = f"erro: {e.__class__.__name__}"

    
    try:
        r = get_redis_client()
        visitas = r.incr("visitas_home")  
        info["redis_status"] = "ok"
        info["visitas_redis"] = visitas
    except Exception as e:
        info["redis_status"] = f"erro: {e.__class__.__name__}"

    return jsonify(info)

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)
