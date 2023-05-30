import sqlite3


class Rating:
    def __init__(self, rating_id, title, year, rating):
        self.rating_id = rating_id
        self.title = title
        self.year = year
        self.rating = rating


def execute_sql(command):
    conn = sqlite3.connect('imdb.db')
    curs = conn.cursor()
    curs.execute(command)
    conn.commit()
    fetch_data = curs.fetchall()
    curs.close()
    conn.close()
    return fetch_data


def get_ratings_from_file(filename):
    ratings_output = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in [f.strip() for f in file.readlines()]:
            rating_info = (r.strip() for r in line.split(','))
            rating_id = next(rating_info)
            title = next(rating_info)
            year = next(rating_info)
            rating = next(rating_info)
            ratings_output.append(Rating(rating_id, title, year, rating))
    return ratings_output


def create_db(input_ratings):
    execute_sql('DROP TABLE IF EXISTS `ratings`;')
    execute_sql('CREATE TABLE ratings (id INTEGER PRIMARY KEY, title VARCHAR(20), year INT, rating FLOAT);')
    for r in input_ratings:
        execute_sql(f'''INSERT INTO ratings (id, title, year, rating) VALUES (
                    {r.rating_id}, '{r.title}', {r.year}, {r.rating});''')


if __name__ == '__main__':
    ratings_file = 'ratings.scv'
    ratings = get_ratings_from_file(ratings_file)
    create_db(ratings)

    all_ratings = execute_sql('SELECT * FROM ratings ORDER BY title;')
    for rating in all_ratings:
        print(rating)

    ratings_more_than = execute_sql('SELECT * FROM ratings WHERE rating > 8.70')
    print('More than 8.7 :')
    for rating in ratings_more_than:
        print(rating)
