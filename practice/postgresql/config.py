from configparser import ConfigParser

config = ConfigParser()
# config.read("./practice/postgresql/config.ini")
config.read("config.ini")
URL = config.get("TG", "URL")
HOST = config.get("TG", "HOST")
USER = config.get("TG", "USER")
DB = config.get("TG", "DB")
PASSWORD = config.get("TG", "PASSWORD")
