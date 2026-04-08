from config import *

app = Flask('APP')

@app.route('/api/help')
def help_api():
    routes = []
    for rule in app.url_map.iter_rules():
        if str(rule) == "/api/sql/<path:cmd>": routes.append(str(rule) + " - use %20 for space and %27 for quotes")
        else: routes.append(str(rule))
    return routes

@app.route('/api/sql/<path:cmd>')
def execute(cmd):
    x, conn = connect()
    x.execute(cmd)
    ret = x.fetchall()
    conn.close()
    return ret(ret)

@app.route('/api/health')
def health():
    return "status ok"

@app.route('/api/schema')
def schema():
    x, conn = connect()
    ret = get_pragmas(x)
    conn.close()
    return ret(ret)

@app.route('/api/countries')
def countries():
    x, conn = connect()
    x.execute(f'SELECT country FROM locations order by country')
    ret = x.fetchall()
    conn.close()
    return ret

@app.route('/api/<country>/locations')
def locations(country):
    x, conn = connect()
    x.execute(f'SELECT location_name FROM locations WHERE country = "{country}"')
    ret = x.fetchall()
    conn.close()
    return ret

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = False)
