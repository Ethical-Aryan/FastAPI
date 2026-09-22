import pymysql
from database.dbconnection import get_connection

# Execute INSERT / UPDATE / DELETE queries
def db_execute(query: str, params: tuple = ()):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        last_id = cursor.lastrowid
    conn.close()
    return last_id

# Execute SELECT query and return one record as a dictionary
def fetch_one(query: str, params: tuple = ()):
    conn = get_connection()
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(query, params)
        result = cursor.fetchone()
    conn.close()
    return result

# Execute SELECT query and return all matching records as dictionaries
def fetch_all(query: str, params: tuple = ()):
    conn = get_connection()
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
    conn.close()
    return result

# Initialize Ecommerce database tables if they do not exist
def init_db():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                icon VARCHAR(100) DEFAULT 'bi bi-tag',
                image VARCHAR(500) DEFAULT '',
                slug VARCHAR(100) DEFAULT '',
                description TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                category_id INT NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                original_price DECIMAL(10, 2) DEFAULT NULL,
                stock INT DEFAULT 0,
                badge VARCHAR(50) DEFAULT 'New',
                image VARCHAR(500) DEFAULT '',
                description TEXT
            )
        """)

        # Seed categories if table is empty
        cursor.execute("SELECT COUNT(*) FROM categories")
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO categories (name, icon, image, slug, description) VALUES
                ('Electronics', 'bi bi-laptop', 'https://images.unsplash.com/photo-1498049794561-7780e7231661?w=500', 'electronics', 'Cutting-edge gadgets & gear'),
                ('Gaming', 'bi bi-controller', 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=500', 'gaming', 'Keyboards, mice & consoles'),
                ('Audio', 'bi bi-headphones', 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500', 'audio', 'Wireless headphones & speakers'),
                ('Smart Home', 'bi bi-house-gear', 'https://images.unsplash.com/photo-1558002038-1055907df827?w=500', 'smart-home', 'Lights & home automation')
            """)
            cursor.execute("""
                INSERT INTO products (title, category_id, price, original_price, stock, badge, image, description) VALUES
                ('Wireless Noise Cancelling Headphones', 3, 199.99, 249.99, 25, 'Hot', 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500', 'Active noise cancellation with 30h battery life.'),
                ('RGB Mechanical Gaming Keyboard', 2, 89.99, 119.99, 40, 'Sale', 'https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=500', 'Tactile switches with customizable backlighting.'),
                ('Ultra-Slim 4K Monitor 27-inch', 1, 329.99, 399.99, 15, 'New', 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500', 'Vibrant 4K IPS display with HDR support.'),
                ('Smart Home Assistant Speaker', 4, 49.99, 69.99, 60, 'Popular', 'https://images.unsplash.com/photo-1543512214-318c7553f230?w=500', 'Voice-controlled assistant speaker with rich sound.')
            """)

        conn.commit()
    conn.close()
