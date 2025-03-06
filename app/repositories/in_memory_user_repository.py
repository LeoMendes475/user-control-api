import os
import json
from typing import List
from app.domain.user import User
from app.interfaces.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self, file_path: str = "database/user.txt"):
        self.file_path = file_path
        # Cria o diretório 'database' se não existir
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        
        self.users = self._load_users()  # Carregar os usuários do arquivo
        self.next_id = max([user.userId for user in self.users], default=0) + 1  # Definir o próximo ID

    def _load_users(self) -> List[User]:
        """Carregar os dados de usuários do arquivo de texto"""
        try:
            with open(self.file_path, "r") as file:
                users_data = json.load(file)
                return [User(**user) for user in users_data]
        except FileNotFoundError:
            # Caso o arquivo não exista, retorna uma lista vazia
            return []

    def _save_users(self):
        """Salvar os dados dos usuários no arquivo de texto"""
        with open(self.file_path, "w") as file:
            json.dump([user.__dict__ for user in self.users], file, indent=4)

    def create(self, user: User) -> User:
        """Criar um novo usuário"""
        user.userId = self.next_id
        self.users.append(user)
        self.next_id += 1
        self._save_users()  # Salva no arquivo
        return user
    
    def get(self, userId: int) -> User | None:
        """Buscar um usuário pelo ID"""
        return next((user for user in self.users if user.userId == userId), None)
    
    def update(self, user: User) -> User | None:
        """Atualizar um usuário"""
        for i, existing_user in enumerate(self.users):
            if existing_user.userId == user.userId:
                self.users[i] = user
                self._save_users()  # Salva no arquivo
                return user
        return None
    
    def delete(self, userId: int) -> None:
        """Deletar um usuário pelo ID"""
        self.users = [user for user in self.users if user.userId != userId]
        self._save_users()  # Salva no arquivo
    
    def list_all(self) -> List[User]:
        """Listar todos os usuários"""
        return self.users
