import psycopg2
from config import load_config


# Подключение к базе данных
conn = psycopg2.connect(
    host="your-host.neon.tech",
    dbname="your-db-name",
    user="your-username",
    password="your-password",
    sslmode="require"
)


# Создаём курсор
cursor = conn.cursor()

# Выполняем запрос для получения имени текущей БД
cursor.execute("SELECT current_database();")
current_db = cursor.fetchone()[0]

print("Текущая база данных:", current_db)

# Закрываем соединение
cursor.close()
conn.close()
