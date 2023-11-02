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

# Docker $ docker run --name power -p 3306:3306 -e MYSQL_ROOT_PASSWORD=12345 -d mysql
# --rm не нужен, чтобы не терялись внесенные измнения
# Подключиться к серверу баз данных и посмотреть имеющиеся базы данных:
# docker exec -it mysqlpower mysql -uroot -p
# SHOW DATABASES;
# exit
# Чтобы зайти через терминал в докере, то надо прописать mysql -p12345 (12345 - это пароль, приклеенный к тегу -p)
# Импорт конфигурации БД
# docker exec -i mysql_instance mysql -uroot -ppassw < C:\Temp\MySQL_SampleDB.sql
# Подключение к MySQL серверу в режиме командной строки непосредственно в контейнере
# docker exec -it mysql_instance mysql -uroot -ppassw
# Создание пользователя для подключения к БД
# CREATE USER 'dba'@'localhost' IDENTIFIED BY 'dbaPass';
# GRANT ALL PRIVILEGES ON *.* TO 'dba'@'localhost' WITH GRANT OPTION;
# CREATE USER 'dba'@'%' IDENTIFIED BY 'dbaPass';
# GRANT ALL PRIVILEGES ON *.* TO 'dba'@'%' WITH GRANT OPTION;
# FLUSH PRIVILEGES;
# exit
# Создать соединение в DBeaver, поменять Key на True
# Готово :)

# CREATE DATABASE mydb;
# USE mydb; - Переключение на нужную БД
