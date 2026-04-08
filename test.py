from config import *

conn = sql.connect('source.db')
x = conn.cursor()
x.execute('select country from locations order by country')
country = 'Poland'
#x.execute(f'SELECT location_name FROM locations WHERE country = "{country}" order by country')
print(x.fetchall())