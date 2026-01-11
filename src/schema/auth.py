from pydantic import BaseModel

class LoginSchema(BaseModel):
	username: str
	password: str

class RegisterSchema(BaseModel):
	username: str
	password: str
# could be more propertise to pass during registration therefore new schema is created