from fastapi import FastAPI, HTTPException
from app.repositories.in_memory_user_repository import InMemoryUserRepository
from app.services.user_service import UserService
from app.use_cases.manage_user import ManageUser
from app.domain.user import User
from pydantic import BaseModel

# Inicializa os componentes do sistema
app = FastAPI()
user_repository = InMemoryUserRepository()
user_service = UserService(user_repository)
manage_user = ManageUser(user_service)

class User(BaseModel):
    name: str
    email: str | None = None

@app.post("/users/")
def create_user(user: User):
    if user is not None:
        raise HTTPException(status_code=404, detail="Missing the information about the user")
    createdUser = manage_user.create_user(user.name, user.email)
    return {"message": "User created", "user": createdUser}

@app.get("/users/{userId}")
def get_user(userId: int):
    user = manage_user.get_user(userId)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/")
def list_users():
    return manage_user.list_users()

@app.put("/users/{userId}")
def update_user(userId: int, name: str, email: str):
    user = manage_user.get_user(userId)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = name
    user.email = email
    updated_user = manage_user.update_user(user)
    return updated_user

@app.delete("/users/{userId}")
def delete_user(userId: int):
    manage_user.delete_user(userId)
    return {"message": "User deleted"}

