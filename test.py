from config import *

conn = sql.connect('source.db')
x = conn.cursor()
x.execute('select country, location_name from locations order by country')
print(ret(x.fetchall()))
z = get_pragmas(x)

#print(z)
#print(ret(z))