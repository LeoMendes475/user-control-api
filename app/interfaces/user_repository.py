# app/interfaces/user_repository.py

from typing import List
from app.domain.user import User

class UserRepository:
    def create(self, user: User) -> User:
        raise NotImplementedError
    
    def get(self, userId: int) -> User:
        raise NotImplementedError
    
    def update(self, user: User) -> User:
        raise NotImplementedError
    
    def delete(self, userId: int) -> None:
        raise NotImplementedError
    
    def list_all(self) -> List[User]:
        raise NotImplementedError
