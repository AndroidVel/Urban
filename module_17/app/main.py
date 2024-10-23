from fastapi import FastAPI
from routers import user, task

app = FastAPI()


@app.get('/')
async def main_page():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(user.router)
app.include_router(task.router)
