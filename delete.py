import psycopg2
from connector import get_connection
host, database, user, password = get_connection()

def delete_records_by_condition(condition):
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

    # Удаление записей из таблицы "salary" по условию
    query = """
        DELETE FROM salary WHERE {}
    """.format(condition)

    cur.execute(query)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    cur.close()
    conn.close()

    print("Записи удалены по условию: {}".format(condition))

# Пример использования функции delete_records_by_condition()
delete_records_by_condition("currency = 'USD'")