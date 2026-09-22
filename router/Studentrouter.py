from fastapi import APIRouter
from typing import Optional
from controller.Studentcontroller import (
    user_register,
    user_login,
    admin_login,
    get_categories,
    create_category,
    delete_category,
    get_products,
    create_product,
    delete_product,
)
from model.Studentmodel import (
    UserRegisterRequest,
    UserLoginRequest,
    AdminLoginRequest,
    CategoryRequest,
    ProductRequest,
)

router = APIRouter()

# ----------------- User Authentication ----------------- #
@router.post("/user/register")
def register_user(request: UserRegisterRequest):
    return user_register(request)

@router.post("/user/login")
def login_user(request: UserLoginRequest):
    return user_login(request)

# ----------------- Admin Authentication ---------------- #
@router.post("/admin/login")
def admin_login_route(request: AdminLoginRequest):
    return admin_login(request)

# ------------------- Categories API -------------------- #
@router.get("/categories")
def list_categories():
    return get_categories()

@router.post("/categories")
def add_category(request: CategoryRequest):
    return create_category(request)

@router.delete("/categories/{category_id}")
def remove_category(category_id: int):
    return delete_category(category_id)

# -------------------- Products API --------------------- #
@router.get("/products")
def list_products(category_id: Optional[int] = None):
    return get_products(category_id)

@router.post("/products")
def add_product(request: ProductRequest):
    return create_product(request)

@router.delete("/products/{product_id}")
def remove_product(product_id: int):
    return delete_product(product_id)
