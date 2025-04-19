import psycopg2
from config import load_config
from tabulate import tabulate

def get_contacts_paginated(limit, offset):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT person_id, name, second_name, last_name, phone
                    FROM phone_book
                    ORDER BY person_id
                    LIMIT %s OFFSET %s;
                """, (limit, offset))
                rows = cur.fetchall()

                if rows:
                    headers = ['ID', 'Name', 'Second Name', 'Last Name', 'Phone']
                    print(tabulate(rows, headers=headers, tablefmt='grid'))
                else:
                    print("Нет данных для отображения.")
    except Exception as e:
        print("Ошибка при получении данных:", e)


if __name__ == '__main__':
    limit = 5
    offset = 0

    while True:
        get_contacts_paginated(limit, offset)
        cmd = input("n-next | p-prev | q-quit: ").strip().lower()
        if cmd == 'n':
            offset += limit
        elif cmd == 'p' and offset >= limit:
            offset -= limit
        elif cmd == 'q':
            break
        else:
            print("Неверная команда.")