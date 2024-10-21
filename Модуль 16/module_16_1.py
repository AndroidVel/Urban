from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def response():
    return {'Главная страница'}


@app.get('/user/admin')
async def response():
    return {'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def response(user_id):
    return {f'Вы вошли как пользователь №{user_id}'}


@app.get('/user')
async def response(username: str = 'User', age: int = 0):
    return {f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
