import mysql.connector

from connect_mysql import connect
from create_tables_queries import (
    create_movies_table_query,
    create_reviewers_table_query,
    create_ratings_table_query,
)


def create_tables_db() -> None:
    # with open("./practice/mysql/create_tables.sql", "r") as f:
    #     mysql_tables = f.read()
    # mysql_tables is not executed by cursor for some reason

    with connect.cursor() as cursor:
        cursor.execute(create_movies_table_query)
        cursor.execute(create_reviewers_table_query)
        cursor.execute(create_ratings_table_query)
        connect.commit()
        print("Tables created")


if __name__ == "__main__":
    create_tables_db()
