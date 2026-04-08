from config import *

conn = sql.connect('source.db')
x = conn.cursor()
x.execute('select country from locations order by country')
country = 'Yemen'
x.execute(f'SELECT * FROM locations')
print(ret(x.fetchall()))
z = get_pragmas(x)

#print(z)
#print(ret(z))