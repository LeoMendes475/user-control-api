from app.domain.user import User
from app.interfaces.user_repository import UserRepository
from app.domain.entities.user_schemas import UserCreate, UserUpdate, UserResponse

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_data: UserCreate) -> UserResponse:
        print(user_data)
        user = User(userId=0, name=user_data.name, email=user_data.email)  # userId será atribuído pelo repositório
        created_user = self.repository.create(user)
        return UserResponse(userId=created_user.userId, name=created_user.name, email=created_user.email)
    
    def get_user(self, userId: int) -> UserResponse | None:
        user = self.repository.get(userId)
        if user:
            return UserResponse(userId=user.userId, name=user.name, email=user.email)
        return None  # FastAPI tratará isso na rota
    
    def update_user(self, userId: int, user_update: UserUpdate) -> UserResponse | None:
        user = self.repository.get(userId)
        if not user:
            return None

        if user_update.name:
            user.name = user_update.name
        if user_update.email:
            user.email = user_update.email

        updated_user = self.repository.update(user)
        return UserResponse(userId=updated_user.userId, name=updated_user.name, email=updated_user.email)
    
    def delete_user(self, userId: int) -> None:
        self.repository.delete(userId)
    
    def list_all(self) -> list[UserResponse]:
        return [UserResponse(userId=user.userId, name=user.name, email=user.email) for user in self.repository.list_all()]
