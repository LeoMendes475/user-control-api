# app/use_cases/manage_user.py

from app.services.user_service import UserService

class ManageUser:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create_user(self, name: str, email: str):
        user = self.user_service.create_user(name, email)
        return user
    
    def get_user(self, userId: int):
        return self.user_service.get_user(userId)

    def update_user(self, user):
        return self.user_service.update_user(user)

    def delete_user(self, userId: int):
        return self.user_service.delete_user(userId)

    def list_users(self):
        return self.user_service.list_users()
