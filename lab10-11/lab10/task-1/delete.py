import psycopg2
from config import load_config

def delete_user_by_value(value):
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM phone_book WHERE name = %s OR phone = %s", (value, value))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

