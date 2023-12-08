import psycopg2
from connector import get_connection
host, database, user, password = get_connection()

conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

if conn != None:
    print('Success connection')
else:
    print('Need to configure your connector')

cur = conn.cursor()

cur.execute("""
    SELECT * FROM salary
""")
rows = cur.fetchall()

for row in rows:
    print(row)


conn.commit()
cur.close()
conn.close()
