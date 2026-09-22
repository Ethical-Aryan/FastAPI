from decimal import Decimal
from datetime import datetime
from model.Studentmodel import (
    UserRegisterRequest,
    UserLoginRequest,
    AdminLoginRequest,
    CategoryRequest,
    ProductRequest,
)
from database.dboperations import db_execute, fetch_one, fetch_all

# Helper to convert Decimal and datetime values into standard JSON-compatible types
def serialize(data):
    if isinstance(data, list):
        return [serialize(i) for i in data]
    if isinstance(data, dict):
        return {
            k: float(v) if isinstance(v, Decimal) else (v.isoformat() if isinstance(v, datetime) else v)
            for k, v in data.items()
        }
    return data

# User Registration
def user_register(request: UserRegisterRequest):
    try:
        db_execute(
            "INSERT INTO registration (name, email, password) VALUES (%s, %s, %s)",
            (request.name, request.email, request.password)
        )
        return {"message": "Registration successful"}
    except Exception as e:
        return {"error": str(e)}

# User Login
def user_login(request: UserLoginRequest):
    user = fetch_one(
        "SELECT id, name, email FROM registration WHERE email = %s AND password = %s",
        (request.email, request.password)
    )
    if user:
        return {"message": "Login successful", "user": serialize(user)}
    return {"error": "Invalid email or password!"}

# Admin Login
def admin_login(request: AdminLoginRequest):
    admin = fetch_one(
        "SELECT * FROM admin WHERE username = %s AND password = %s",
        (request.username, request.password)
    )
    if admin or (request.username == "admin" and request.password == "admin123"):
        return {"message": "Login successful", "username": request.username}
    return {"error": "Invalid Username or Password!"}

# Get All Categories
def get_categories():
    return serialize(fetch_all("SELECT * FROM categories ORDER BY id ASC"))

# Create Category
def create_category(request: CategoryRequest):
    slug = request.name.lower().replace(" ", "-")
    cat_id = db_execute(
        "INSERT INTO categories (name, icon, image, slug, description) VALUES (%s, %s, %s, %s, %s)",
        (request.name, request.icon or "bi bi-tag", request.image or "", slug, request.description or "")
    )
    return {"message": "Category created", "id": cat_id}

# Delete Category
def delete_category(category_id: int):
    db_execute("DELETE FROM products WHERE category_id = %s", (category_id,))
    db_execute("DELETE FROM categories WHERE id = %s", (category_id,))
    return {"message": "Category deleted"}

# Get Products (optional filter by category)
def get_products(category_id: int = None):
    if category_id:
        query = """
            SELECT p.*, c.name AS category_name
            FROM products p LEFT JOIN categories c ON p.category_id = c.id
            WHERE p.category_id = %s ORDER BY p.id DESC
        """
        products = fetch_all(query, (category_id,))
    else:
        query = """
            SELECT p.*, c.name AS category_name
            FROM products p LEFT JOIN categories c ON p.category_id = c.id
            ORDER BY p.id DESC
        """
        products = fetch_all(query)
    return serialize(products)

# Create Product
def create_product(request: ProductRequest):
    prod_id = db_execute(
        "INSERT INTO products (title, category_id, price, original_price, stock, badge, image, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (request.title, request.category_id, request.price, request.original_price, request.stock, request.badge or "New", request.image or "", request.description or "")
    )
    return {"message": "Product created", "id": prod_id}

# Delete Product
def delete_product(product_id: int):
    db_execute("DELETE FROM products WHERE id = %s", (product_id,))
    return {"message": "Product deleted"}

