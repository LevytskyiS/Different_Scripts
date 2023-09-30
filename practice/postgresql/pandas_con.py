import pandas as pd
import psycopg2

from config import settings
from connect_db import SQL_ALCHEMY_DATABASE_URL

conn = psycopg2.connect(
    host=settings.HOST,
    dbname=settings.DB,
    user=settings.USER,
    password=settings.PASSWORD,
)

query = "SELECT * FROM students"

cursor = conn.cursor()
cursor.execute(query)

df = pd.DataFrame(cursor.fetchall())

print(df.head())

# ALTERNATIVE
# sql = "SELECT * FROM students"
# df = pd.read_sql(sql, SQL_ALCHEMY_DATABASE_URL)
# print(df)
