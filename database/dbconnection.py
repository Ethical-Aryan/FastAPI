import pymysql

try:
    db_host = "localhost"
    db_name = "ecommerce"
    db_username = "root"
    db_password = ""

    conn = pymysql.connect(
        host = db_host,
        database = db_name,
        user = db_username,
        password = db_password
    )
    print( f"Connection Successfull with : {db_name}")
except Exception as e:
    print(f"Connection Unsuccessfull :  {str(e)}")
