import mysql.connector
from mysql.connector import errorcode

from config import settings

config = {
    "user": settings.USER,
    "password": settings.PASSWORD,
    "host": settings.HOST,
    "database": settings.DB,
    "raise_on_warnings": True,
}


def get_connect():
    connect = None
    try:
        connect = mysql.connector.connect(**config)
        print("Connected to MySQL DB")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return connect


connect = get_connect()
