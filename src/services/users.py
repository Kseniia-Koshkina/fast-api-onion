from src.models.users import Users
from src.repository.abstract import AbstractUserRepository
from src.utils.auth import verify_password

class UserService():
	def __init__(self, repository):
		self.repository: AbstractUserRepository = repository

	def get_user(self, user_name):
		return self.repository.get_by_username(user_name)

	def create_user(self, user_data: Users):
		user_exists = self.get_user(user_data.username)

		if user_exists:
			raise ValueError("User with this username already exists")

		new_user: Users = self.repository.create(user_data)
		return new_user.id

	def validate_user(self, username, password):
		user: Users = self.get_user(username)
		if not user:
			return False
		if not verify_password(password, user.password_hash):
			return False
		return True
