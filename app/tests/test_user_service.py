# tests/test_user_service.py

import unittest
from app.repositories.in_memory_user_repository import InMemoryUserRepository
from app.services.user_service import UserService
from app.domain.user import User

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.repository = InMemoryUserRepository()
        self.service = UserService(self.repository)

    def test_create_user(self):
        user = self.service.create_user("Alice", "alice@example.com")
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.email, "alice@example.com")

    def test_get_user(self):
        user = self.service.create_user("Bob", "bob@example.com")
        fetched_user = self.service.get_user(user.userId)
        self.assertEqual(fetched_user.name, "Bob")

    def test_update_user(self):
        user = self.service.create_user("Charlie", "charlie@example.com")
        user.name = "Charlie Brown"
        updated_user = self.service.update_user(user)
        self.assertEqual(updated_user.name, "Charlie Brown")

    def test_delete_user(self):
        user = self.service.create_user("David", "david@example.com")
        self.service.delete_user(user.userId)
        deleted_user = self.service.get_user(user.userId)
        self.assertIsNone(deleted_user)

if __name__ == "__main__":
    unittest.main()
