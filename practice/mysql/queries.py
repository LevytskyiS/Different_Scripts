import mysql.connector

from connect_mysql import connect


# Different queris for different tables in the database
def describe_db():
    show_table_query = "DESCRIBE movies"
    with connect.cursor() as cursor:
        cursor.execute(show_table_query)
        # Fetch rows from last executed query
        result = cursor.fetchall()
        connect.close()
        for row in result:
            print(row)


# describe_db()


def modify_movie_table():
    alter_table_query = """
    ALTER TABLE movies
    MODIFY COLUMN collection_in_mil DECIMAL(4,1)
    """
    show_table_query = "DESCRIBE movies"
    with connect.cursor() as cursor:
        cursor.execute(alter_table_query)
        cursor.execute(show_table_query)
        # Получить строки из последнего выполненного запроса
        result = cursor.fetchall()
        print("Movie table scheme after modifying:")
        for row in result:
            print(row)


# modify_movie_table()


def drop_table():
    drop_table_query = "DROP TABLE ratings"
    with connect.cursor() as cursor:
        cursor.execute(drop_table_query)


def fill_data_movies_execute():
    insert_movies_query = """
    INSERT INTO movies (title, release_year, genre, collection_in_mil)
    VALUES
        ("Forrest Gump", 1994, "Drama", 330.2),
        ("3 Idiots", 2009, "Drama", 2.4),
        ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
        ("Good Will Hunting", 1997, "Drama", 138.1),
        ("Skyfall", 2012, "Action", 304.6),
        ("Gladiator", 2000, "Action", 188.7),
        ("Black", 2005, "Drama", 3.0),
        ("Titanic", 1997, "Romance", 659.2),
        ("The Shawshank Redemption", 1994, "Drama",28.4),
        ("Udaan", 2010, "Drama", 1.5),
        ("Home Alone", 1990, "Comedy", 286.9),
        ("Casablanca", 1942, "Romance", 1.0),
        ("Avengers: Endgame", 2019, "Action", 858.8),
        ("Night of the Living Dead", 1968, "Horror", 2.5),
        ("The Godfather", 1972, "Crime", 135.6),
        ("Haider", 2014, "Action", 4.2),
        ("Inception", 2010, "Adventure", 293.7),
        ("Evil", 2003, "Horror", 1.3),
        ("Toy Story 4", 2019, "Animation", 434.9),
        ("Air Force One", 1997, "Drama", 138.1),
        ("The Dark Knight", 2008, "Action",535.4),
        ("Bhaag Milkha Bhaag", 2013, "Sport", 4.1),
        ("The Lion King", 1994, "Animation", 423.6),
        ("Pulp Fiction", 1994, "Crime", 108.8),
        ("Kai Po Che", 2013, "Sport", 6.0),
        ("Beasts of No Nation", 2015, "War", 1.4),
        ("Andadhun", 2018, "Thriller", 2.9),
        ("The Silence of the Lambs", 1991, "Crime", 68.2),
        ("Deadpool", 2016, "Action", 363.6),
        ("Drishyam", 2015, "Mystery", 3.0)
    """
    with connect.cursor() as cursor:
        cursor.execute(insert_movies_query)
        connect.commit()


# fill_data_movies_execute()


def fill_data_reviewers_executemany():
    insert_reviewers_query = """
    INSERT INTO reviewers
    (first_name, last_name)
    VALUES ( %s, %s )
    """
    reviewers_records = [
        ("Chaitanya", "Baweja"),
        ("Mary", "Cooper"),
        ("John", "Wayne"),
        ("Thomas", "Stoneman"),
        ("Penny", "Hofstadter"),
        ("Mitchell", "Marsh"),
        ("Wyatt", "Skaggs"),
        ("Andre", "Veiga"),
        ("Sheldon", "Cooper"),
        ("Kimbra", "Masters"),
        ("Kat", "Dennings"),
        ("Bruce", "Wayne"),
        ("Domingo", "Cortes"),
        ("Rajesh", "Koothrappali"),
        ("Ben", "Glocker"),
        ("Mahinder", "Dhoni"),
        ("Akbar", "Khan"),
        ("Howard", "Wolowitz"),
        ("Pinkie", "Petit"),
        ("Gurkaran", "Singh"),
        ("Amy", "Farah Fowler"),
        ("Marlon", "Crafford"),
    ]
    with connect.cursor() as cursor:
        cursor.executemany(insert_reviewers_query, reviewers_records)
        connect.commit()


# fill_data_reviewers_executemany()


def fill_data_ratings_executemany():
    insert_ratings_query = """
    INSERT INTO ratings
    (rating, movie_id, reviewer_id)
    VALUES ( %s, %s, %s)
    """
    ratings_records = [
        (6.4, 17, 5),
        (5.6, 19, 1),
        (6.3, 22, 14),
        (5.1, 21, 17),
        (5.0, 5, 5),
        (6.5, 21, 5),
        (8.5, 30, 13),
        (9.7, 6, 4),
        (8.5, 24, 12),
        (9.9, 14, 9),
        (8.7, 26, 14),
        (9.9, 6, 10),
        (5.1, 30, 6),
        (5.4, 18, 16),
        (6.2, 6, 20),
        (7.3, 21, 19),
        (8.1, 17, 18),
        (5.0, 7, 2),
        (9.8, 23, 3),
        (8.0, 22, 9),
        (8.5, 11, 13),
        (5.0, 5, 11),
        (5.7, 8, 2),
        (7.6, 25, 19),
        (5.2, 18, 15),
        (9.7, 13, 3),
        (5.8, 18, 8),
        (5.8, 30, 15),
        (8.4, 21, 18),
        (6.2, 23, 16),
        (7.0, 10, 18),
        (9.5, 30, 20),
        (8.9, 3, 19),
        (6.4, 12, 2),
        (7.8, 12, 22),
        (9.9, 15, 13),
        (7.5, 20, 17),
        (9.0, 25, 6),
        (8.5, 23, 2),
        (5.3, 30, 17),
        (6.4, 5, 10),
        (8.1, 5, 21),
        (5.7, 22, 1),
        (6.3, 28, 4),
        (9.8, 13, 1),
    ]
    with connect.cursor() as cursor:
        cursor.executemany(insert_ratings_query, ratings_records)
        connect.commit()


# fill_data_ratings_executemany()


def first_five_movies():
    select_movies_query = "SELECT * FROM movies LIMIT 5"
    with connect.cursor() as cursor:
        cursor.execute(select_movies_query)
        result = cursor.fetchall()
        for row in result:
            print(row)


# first_five_movies()


def most_earned_movies():
    select_movies_query = """
    SELECT title, collection_in_mil
    FROM movies
    WHERE collection_in_mil > 300
    ORDER BY collection_in_mil DESC
    """
    with connect.cursor() as cursor:
        cursor.execute(select_movies_query)
        for movie in cursor.fetchall():
            print(movie)


# most_earned_movies()


def concatenated_query():
    select_movies_query = """
    SELECT CONCAT(title, " (", release_year, ")"),
        collection_in_mil
    FROM movies
    ORDER BY collection_in_mil DESC
    LIMIT 5
    """
    with connect.cursor() as cursor:
        cursor.execute(select_movies_query)
        for movie in cursor.fetchall():
            print(movie)


# concatenated_query()


def fetchmany_query():
    select_movies_query = """
    SELECT CONCAT(title, " (", release_year, ")"),
        collection_in_mil
    FROM movies
    ORDER BY collection_in_mil DESC
    """
    with connect.cursor() as cursor:
        cursor.execute(select_movies_query)
        for movie in cursor.fetchmany(size=5):
            print(movie)
        cursor.fetchall()  # It is needed to remove all other results which were not read by fetchmany


# fetchmany_query()


def inner_join_query():
    select_movies_query = """
    SELECT CONCAT(first_name, " ", last_name), COUNT(*) as num
    FROM reviewers
    INNER JOIN ratings
        ON reviewers.id = ratings.reviewer_id
    GROUP BY reviewer_id
    ORDER BY num DESC
    LIMIT 1
    """
    with connect.cursor() as cursor:
        cursor.execute(select_movies_query)
        for movie in cursor.fetchall():
            print(movie)


# inner_join_query()


def update_data():
    update_query = """
    UPDATE
        reviewers
    SET
        last_name = "Cooper"
    WHERE
        first_name = "Amy"
    """
    with connect.cursor() as cursor:
        cursor.execute(update_query)
        connect.commit()


# update_data()


def delete_query():
    # First of all we have to check if the data we want to delete exists
    # select_movies_query = """
    # SELECT reviewer_id, movie_id FROM ratings
    # WHERE reviewer_id = 2
    # """
    # with connect.cursor() as cursor:
    #     cursor.execute(select_movies_query)
    #     for movie in cursor.fetchall():
    #         print(movie)

    delete_query = "DELETE FROM reviewers WHERE id = 2"
    with connect.cursor() as cursor:
        cursor.execute(delete_query)
        connect.commit()


# delete_query()


def newest_movies():
    select_query = """
    SELECT * FROM movies
    WHERE release_year >= 2010
    GROUP BY release_year
    """
    with connect.cursor() as cursor:
        cursor.execute(select_query)
        for row in cursor.fetchall():
            print(row)


newest_movies()
