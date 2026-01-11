from fastapi import APIRouter, Depends

from src.services.users import UserService
from src.dependencies.services import get_users_service
from src.schema.auth import LoginSchema

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

    return {"jwt_token": "fake-jwt-token"}


@router.post("/register")
def register(
	login_data: LoginSchema,
	user_service: UserService = Depends(get_users_service)
):
	user = user_service.create_user(login_data)
	return user


