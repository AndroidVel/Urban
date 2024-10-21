from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
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


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_user(user: User, username: str, age: int) -> User:
    if len(users) != 0:
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
