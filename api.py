from config import *

app = Flask('APP')

@app.route('/help')
def help():
    return jsonify({"/api/health"})

@app.route('/api/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/api/weather/<city>')
def get_weather(city):
    x.execute("SELECT * FROM rc WHERE city = ? LIMIT 1", (city,))
    row = x.fetchone()
    
    if row:
        return jsonify(dict(zip([desc[0] for desc in x.description], row)))
    return jsonify({"error": "City not found"}), 404

@app.route('/api/weather')
def get_all_weather():
    x.execute("SELECT country, city, condition, lat, lon FROM rc LIMIT 20")
    rows = x.fetchall()
    return jsonify([dict(zip([desc[0] for desc in x.description], row)) for row in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
