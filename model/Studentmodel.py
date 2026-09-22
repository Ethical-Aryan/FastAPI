from pydantic import BaseModel
from typing import Optional

# Request schema for user registration
class UserRegisterRequest(BaseModel):
    name: str
    email: str
    password: str

# Backward compatibility alias
StudentRequest = UserRegisterRequest

# Request schema for user login
class UserLoginRequest(BaseModel):
    email: str
    password: str

# Request schema for admin login
class AdminLoginRequest(BaseModel):
    username: str
    password: str

# Request schema for adding a category
class CategoryRequest(BaseModel):
    name: str
    icon: Optional[str] = "bi bi-tag"
    image: Optional[str] = ""
    description: Optional[str] = ""

# Request schema for adding a product
class ProductRequest(BaseModel):
    title: str
    category_id: int
    price: float
    original_price: Optional[float] = None
    stock: int = 0
    badge: Optional[str] = "New"
    image: Optional[str] = ""
    description: Optional[str] = ""
