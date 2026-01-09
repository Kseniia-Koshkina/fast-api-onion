from fastapi import FastAPI
import uvicorn
from Models.tasks import Tasks
from db.connection import database_session

app = FastAPI()

@app.get("/")
def read_root():
  db = database_session()
  tasks = db.query(Tasks).all()
  return {"tasks": tasks}


if __name__ == "__main__":
  uvicorn.run(app="main:app", reload=True)