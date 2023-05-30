import csv
import sqlite3

def create_ratings_table():
    conn = sqlite3.connect('imdb.db')
    cursor = conn.cursor()

    # Створення таблиці ratings
    cursor.execute('''CREATE TABLE IF NOT EXISTS ratings
                      (id INTEGER PRIMARY KEY, title VARCHAR(20), year INT, rating FLOAT)''')

    conn.commit()
    conn.close()

def insert_ratings_data():
    conn = sqlite3.connect('imdb.db')
    cursor = conn.cursor()

    # Відкриття і зчитування даних з файлу imdb.csv
    with open('imdb.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустити заголовки

        # Вставка даних у таблицю ratings
        for row in reader:
            cursor.execute("INSERT INTO ratings (title, year, rating) VALUES (?, ?, ?)",
                           (row[0], int(row[1]), float(row[2])))

    conn.commit()
    conn.close()

def fetch_all_ratings():
    conn = sqlite3.connect('imdb.db')
    cursor = conn.cursor()

    # Зчитування та виведення значень таблиці ratings в алфавітному порядку за полем title
    cursor.execute("SELECT * FROM ratings ORDER BY title ASC")
    rows = cursor.fetchall()

    print("Значення таблиці ratings (в алфавітному порядку за полем title):")
    for row in rows:
        print(row)

    conn.close()

def fetch_high_ratings():
    conn = sqlite3.connect('imdb.db')
    cursor = conn.cursor()

    # Зчитування та виведення записів таблиці ratings з ретингом більшим за 8.70
    cursor.execute("SELECT * FROM ratings WHERE rating > 8.70")
    rows = cursor.fetchall()

    print("Записи таблиці ratings з ретингом більшим за 8.70:")
    for row in rows:
        print(row)

    conn.close()

# Створення таблиці ratings
create_ratings_table()

# Вставка даних з файлу imdb.csv у таблицю ratings
insert_ratings_data()

# Зчитування та виведення усіх значень таблиці ratings
fetch_all_ratings()

# Зчитування та виведення записів таблиці ratings з ретингом більшим за 8.70
fetch_high_ratings()