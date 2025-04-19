import psycopg2
from csv import DictReader
from config import load_config

def insert(name, second_name, last_name, phone_number):
    config = load_config()    
    person_id = None

    try:
        with psycopg2.connect(**config) as connection:
            print("Connected")
            with connection.cursor() as cursor:
                cursor.execute(
                        "INSERT INTO phone_book(name, second_name, last_name, phone) VALUES (%s, %s, %s, %s) RETURNING person_id;",
                        (name, second_name, last_name, phone_number)
                    )
                rows = cursor.fetchone()
                if rows:
                    person_id = rows[0]
                connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return person_id
    
