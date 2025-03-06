# app/domain/user.py
from typing import Optional

class User:
    def __init__(self, name: str, email: str, userId: Optional[int] = None,):
        self.userId = userId
        self.name = name
        self.email = email

    def __str__(self):
        return f"User {self.name} (ID: {self.userId})"
