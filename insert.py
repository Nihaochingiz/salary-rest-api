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

# Insert test data
data = [
    ("John Doe1", 5000.0, "USD"),
    ("Jane Smith1", 4000.0, "EUR"),
    ("Alex Johnson1", 6000.0, "GBP"),
    ("Сергей Николаевич", 5000.0, "USD"),
    ("Владимир Петрович", 4000.0, "EUR"),
    ("Анна Николаевна", 6000.0, "GBP")
]

for record in data:

   cur.execute("""
        INSERT INTO salary (employee_name, amount, currency)
       VALUES (%s, %s, %s)
     """, record)

# Save the changes and close the connection
conn.commit()
cur.close()
conn.close()

print("Тестовые записи добавлены.")