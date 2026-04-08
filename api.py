from config import *

app = Flask('weather-api')
DB_PATH = os.path.join(os.path.dirname('recent_capitol_final.db'), '')

@app.route('/api/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/api/weather/<city>')
def get_weather(city):
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rc WHERE city = ? LIMIT 1", (city,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return jsonify(dict(zip([desc[0] for desc in cursor.description], row)))
    return jsonify({"error": "City not found"}), 404

@app.route('/api/weather')
def get_all_weather():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT country, city, condition, lat, lon FROM rc LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([dict(zip([desc[0] for desc in cursor.description], row)) for row in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
