import pymysql
from database.dbconnection import get_connection

# Function to execute INSERT / UPDATE / DELETE queries
def db_insert(query: str, params: tuple):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
    conn.close()

# Function to execute SELECT queries and fetch a single record as a dictionary
def fetch_one(query: str, params: tuple):
    conn = get_connection()
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(query, params)
        result = cursor.fetchone()
    conn.close()
    return result


