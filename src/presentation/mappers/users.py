from ..schema.auth import UserRegisterSchema
from ..dto.users import UserCreateDTO

def user_register_to_dto(user_register: UserRegisterSchema) -> UserCreateDTO:
    return UserCreateDTO(
        username=user_register.username,
        password=user_register.password
    )