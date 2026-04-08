from config import *

app = Flask('APP')

@app.route('/api/help')
def help():
    return jsonify(['/api/health', '/api/countries', '/api/schema', '/api/<country>/locations', '/api/sql/cmd - use %20 instead of spaces'])

@app.route('/api/sql/<path:cmd>')
def execute(cmd):
    x, conn = connect()
    x.execute(cmd)
    conn.close()
    return jsonify(x.fetchall())

@app.route('/api/health')
def health():
    return jsonify("status ok")

@app.route('/api/schema')
def schema():
    x, conn = connect()
    conn.close()
    return jsonify(get_pragmas(x))

@app.route('/api/countries')
def countries():
    x, conn = connect()
    x.execute(f'SELECT country FROM locations')
    rows = x.fetchall()
    countries = [row[0] for row in rows]
    conn.close()
    return jsonify(countries)

@app.route('/api/<country>/locations')
def locations(country):
    x, conn = connect()
    x.execute(f'SELECT location_name FROM locations WHERE country = ?', (country,))
    rows = x.fetchall()
    locations = [row[0] for row in rows]
    conn.close()
    return jsonify(locations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
