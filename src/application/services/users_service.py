from src.presentation.dto.users import UserCreateDTO
from src.domain.models.users_domain_model import Users
from src.domain.repositories.abstract_users_repository import AbstractUserRepository
from src.utils.auth import generate_password_hash, verify_password

class UserService():
	def __init__(self, repository):
		self.repository: AbstractUserRepository = repository

	def get_user(self, user_name):
		return self.repository.get_by_username(user_name)

	def create_user(self, user_data: UserCreateDTO) -> Users:
		user_exists = self.get_user(user_data.username)

		if user_exists:
			raise ValueError("User with this username already exists")

		password_hash = generate_password_hash(user_data.password)

		new_user = Users(username=user_data.username, password_hash=password_hash)
		user = self.repository.create(new_user)
		return user

	def validate_user(self, username, password):
		user: Users = self.get_user(username)
		if not user:
			return False
		if not verify_password(password, user.password_hash):
			return False
		return True
