from fastapi import FastAPI, HTTPException, Request, Form, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


def user_find(user_id):
    global users
    for id in range(len(users)):
        if users[id].id == user_id:
            return users[id]
    raise IndexError


@app.get('/')
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('user.html', {'request': request, 'users': users})


@app.get('/users/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse('user.html', {'request': request, 'user': user_find(user_id)})
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.post('/user/{username}/{age}')
async def create_user(user: User, username: str, age: int) -> User:
    if users:
        user_id = len(users) + 1
    else:
        user_id = 1
    user.id = user_id
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        edit_user = user_find(user_id)
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    try:
        deleted_user = user_find(user_id)
        users.pop(users.index(user_find(user_id)))
        return deleted_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
