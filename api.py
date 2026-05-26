from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

def get_db():
    # Bazaning to'liq yo'lini aniqlash
    db_path = os.path.join(os.path.dirname(__file__), 'qarzlar.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/qarzlar', methods=['GET'])
def get_qarzlar():
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT id, ism, usd_qarz, uzs_qarz, olingan_sana, beriladigan_sana, izoh FROM mijozlar")
        rows = c.fetchall()
        conn.close()
        return jsonify([dict(row) for row in rows])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/jami', methods=['GET'])
def get_jami():
    try:
        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT SUM(usd_qarz) as jami_usd, SUM(uzs_qarz) as jami_uzs, COUNT(*) as soni FROM mijozlar")
        row = c.fetchone()
        conn.close()
        return jsonify(dict(row))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)