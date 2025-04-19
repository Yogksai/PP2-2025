import psycopg2
from config import load_config

def delete_by_any_column(value):
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM phone_book WHERE name = %s OR phone = %s", (value, value))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    value = input("Enter the name or phone number to delete: ")
    delete_by_any_column(value)