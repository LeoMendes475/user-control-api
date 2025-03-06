from fastapi import APIRouter, Depends, HTTPException
from app.services.user_service import UserService
from app.domain.entities.user_schemas import UserCreate, UserUpdate, UserResponse
from app.repositories.in_memory_user_repository import InMemoryUserRepository

# Função para pegar a instância do serviço de usuário
def get_user_service():
    repository = InMemoryUserRepository()  # Corrigido para instanciar o repositório
    return UserService(repository)

router = APIRouter(prefix="/user", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    # Cria um novo usuário com base nos dados recebidos
    return service.create_user(user)

@router.get("/{userId}", response_model=UserResponse)
def get_user(userId: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(userId)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[UserResponse])
def list_all(service: UserService = Depends(get_user_service)):
    return service.list_all()

@router.put("/{userId}", response_model=UserResponse)
def update_user(userId: int, user_update: UserUpdate, service: UserService = Depends(get_user_service)):
    user = service.get_user(userId)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = service.update_user(userId, user_update)
    return updated_user

@router.delete("/{userId}")
def delete_user(userId: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(userId)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    service.delete_user(userId)
    return {"message": "User deleted successfully"}
