from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("qarzlar.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/qarzlar')
def get_qarzlar():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT id, ism, usd_qarz, uzs_qarz, olingan_sana, beriladigan_sana, izoh FROM mijozlar")
    rows = c.fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

@app.route('/api/jami')
def get_jami():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT SUM(usd_qarz), SUM(uzs_qarz), COUNT(*) FROM mijozlar")
    total_usd, total_uzs, count = c.fetchone()
    conn.close()
    return jsonify({'jami_usd': total_usd or 0, 'jami_uzs': total_uzs or 0, 'soni': count or 0})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)