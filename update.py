import psycopg2
from connector import get_connection
host, database, user, password = get_connection()

def update_records_by_condition(condition, update_values):
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    if conn is not None:
        print('Соединение успешно')
    else:
        print('Настройте коннектор')

    cur = conn.cursor()

    # query for update in table salary
    query = """
        UPDATE salary 
        SET {}
        WHERE {}
    """.format(update_values, condition)

    cur.execute(query)

    # Update EUR in currency RUB
    query_eur_to_rub = """
        UPDATE salary
        SET amount = amount * 90.0  -- Коэффициент конвертации EUR -> RUB
        WHERE currency = 'EUR'
    """

    cur.execute(query_eur_to_rub)

    # Save changes
    conn.commit()
    cur.close()
    conn.close()

    print("Записи обновлены по условию: {}".format(condition))

# Example of use update_records_by_condition()
condition = "currency = 'USD'"
update_values = "amount = amount + 100"
update_records_by_condition(condition, update_values)