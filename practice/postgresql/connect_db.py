from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from config import URL, USER, HOST, DB, PASSWORD

SQL_ALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB}"
# SQL_ALCHEMY_DATABASE_URL = f"postgresql://bs_practice:258466@localhost/bs_db"


def connect_to_db(url: str):
    try:
        engine = create_engine(url)
        print("Connected to DB")
    except Exception as e:
        print("Error connecting to DB\n", e)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


session = connect_to_db(SQL_ALCHEMY_DATABASE_URL)

# FOR POSTGRES
# docker run --name bs_postgres -p 5432:5432 -e POSTGRES_USER=bs_practice -e POSTGRES_PASSWORD=258466 -e POSTGRES_DB=bs_db -d postgres
# bs_postgres - Container name
# 5432:5432 - Ports
# POSTGRES_USER=bs_practice
# POSTGRES_PASSWORD=258466
# POSTGRES_DB=bs_db
# postgres - database


""" 
Now we can execute CRUD operations using 'session'.

It's important to use the follwoing methods: 
    close();
    commit(); 
    rollback();
    cursor().
"""
