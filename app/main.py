from fastapi import FastAPI
from api.routes.todo import todo_router
from api.routes.user import user_router


app = FastAPI()
app.include_router(todo_router)
app.include_router(user_router)


@app.get("/")
def index():
    return {"status": "todo api is running"}
