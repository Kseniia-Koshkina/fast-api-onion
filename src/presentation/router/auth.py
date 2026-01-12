from fastapi import APIRouter, Depends

from ..mappers.users import user_register_to_dto
from src.application.services.users_service import UserService
from src.dependencies.services import get_users_service
from ..schema.auth import LoginSchema, UserRegisterSchema
from src.utils.auth import create_token

router = APIRouter(
	prefix="/auth",
	tags=["auth"]
)

@router.post("/login")
def login(
	user_data: LoginSchema,
	user_service: UserService = Depends(get_users_service)
):
    credentials_valid = user_service.validate_user(
        user_data.username, 
        user_data.password
	)

    if not credentials_valid:
        return {"message": "Invalid username or password"}

    return create_token({"username": user_data.username})


@router.post("/register")
def register(
	login_data: UserRegisterSchema,
	user_service: UserService = Depends(get_users_service)
):
    dto = user_register_to_dto(login_data)
    user = user_service.create_user(dto)
    return create_token({"username": user.username})
