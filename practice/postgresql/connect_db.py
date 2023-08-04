from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings

SQL_ALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.USER}:{settings.PASSWORD}@{settings.HOST}/{settings.DB}"
)


def connect_to_db(url: str):
    try:
        engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
        print("Connected to DB")
    except Exception as e:
        print("Error connecting to DB\n", e)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


session = connect_to_db(SQL_ALCHEMY_DATABASE_URL)


""" 
Now we can execute CRUD operations using 'session'.

It's important to use the follwoing methods: 
    close();
    commit(); 
    rollback();
    cursor().
"""
