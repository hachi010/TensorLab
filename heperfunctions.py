from config import *
import psycopg2
from constants import *
from queries import queries

def get_logger(name, level='DEBUG'):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger

def format_userinfo(rows,col_names):
    users_dict = {}
    for row in rows:
        user_name = row[3]
        users_dict[user_name] = {}
        for counter,col_name in enumerate(col_names):
            # if col_name!='fullname':
            users_dict[user_name][col_name] = row[counter]
    return users_dict

def create_db_connection():
    conn = psycopg2.connect(
        dbname=DBNAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    
    )

    return conn
