import psycopg2
from config import load_config
from create import insert

def update_by_id(person_id, new_name=None, new_phone=None):
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                if new_name:
                    cursor.execute("UPDATE phone_book SET name = %s WHERE person_id = %s", (new_name, person_id))
                if new_phone:
                    cursor.execute("UPDATE phone_book SET phone = %s WHERE person_id = %s", (new_phone, person_id))
                conn.commit()
                print("User updated.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
