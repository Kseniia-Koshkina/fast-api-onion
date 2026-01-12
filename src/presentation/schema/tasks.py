from pydantic import BaseModel

class TaskSchema(BaseModel):
    id: int
    name: str

class TaskAddSchema(BaseModel):
    name: str