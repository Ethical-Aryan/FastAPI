import pymysql

# Step 1: Connect to MySQL Database (XAMPP default: root / no password)
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="ecommerce"
    )

