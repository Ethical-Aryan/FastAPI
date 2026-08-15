import pymysql
from dbconnection import db_connect

conn = db_connect()
cursor = conn.cursor()

cursor.execute("Select * from admin")
result = cursor.fetchall()
print(result)

def insert():
    try:
        query = "Insert into registration (name,email,PASSWORD ) values('Aryan','aryan@gmail.com','aryan123')"
        cursor.execute(query)
        cursor.execute("Select * from registration")
        result = cursor.fetchall()
        print(result)
        conn.commit()
        cursor.close()
        # conn.close()
    except Exception as e:
         return (f"The error is : {str(e)}")


insert()
