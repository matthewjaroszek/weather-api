from config import *

app = Flask('APP')

@app.route('/api/help')
def help():
    return jsonify(['/api/health', '/api/countries'])

@app.route('/api/health')
def health():
    return jsonify("status ok")

@app.route('/api/schema')
def schema():
    x, conn = connect()
    return get_pragmas(x)

@app.route('/api/countries')
def countries():
    x, conn = connect()
    x.execute(f'SELECT country FROM locations')
    rows = x.fetchall()
    countries = [row[0] for row in rows]
    x.close()
    return jsonify(countries)

@app.route('/api/<country>/locations')
def locations(country):
    x, conn = connect()
    x.execute(f'SELECT locations_name FROM locations WHERE country = "{country}"')
    rows = x.fetchall()
    locations = [row[0] for row in rows]
    conn.close()
    return jsonify(locations)

"""
@app.route('/api/weather/<city>')
def get_weather(city):
    x.execute("SELECT * FROM rc WHERE city = ? LIMIT 1", (city,))
    row = x.fetchone()
    
    if row:
        return jsonify(dict(zip([desc[0] for desc in x.description], row)))
    return jsonify({"error": "Cit not found"}), 404

@app.route('/api/weather')
def get_all_weather():
    x.execute("SELECT country, city, condition, lat, lon FROM rc LIMIT 20")
    rows = x.fetchall()
    return jsonify([dict(zip([desc[0] for desc in x.description], row)) for row in rows])
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
