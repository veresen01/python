

'''Задание №3
Создать API для добавления нового пользователя в базу данных. Приложение
должно иметь возможность принимать POST запросы с данными нового
пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Реализуйте валидацию данных запроса и ответа
Задание №4
Создать API для обновления информации о пользователе в базе данных.
Приложение должно иметь возможность принимать PUT запросы с данными
пользователей и обновлять их в базе данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для обновления информации о пользователе (метод PUT).
Реализуйте валидацию данных запроса и ответа.
Задание №5
Создать API для удаления информации о пользователе из базы данных.
Приложение должно иметь возможность принимать DELETE запросы и
удалять информацию о пользователе из базы данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для удаления информации о пользователе (метод DELETE).
Реализуйте проверку наличия пользователя в списке и удаление его из
списка.'''

import uvicorn
from fastapi import FastAPI,HTTPException
import logging
from pydantic import BaseModel



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email:str
    password: str

users=[
    User(id=0, name ='test', email='test@example.com', password='kfkfgkfkg')
]

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get('/user/', response_model=list[User])
async def get_users():
    return users

@app.get('/users/{id}', response_model=User)
async def get_user(id:int):
    user=[user for user in users if  user.id==id]
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user[0]

@app.post('/user/', response_model=User)
async def create_user(user: User):
    if [u for u in users if u.id==user.id]:
        raise HTTPException(status_code=409, detail="User already exist")
    users.append(user)
    return user

@app.put('/user/', response_model=User)
async  def update_user(user:User):
    for ind in range(len(users)):
        if users[ind].id==user.id:
            users[ind]=user
            return users[ind]
    raise HTTPException(status_code=404, detail="User not found")

@app.delete('/User/')
async  def delete_user(id:int):
    for ind in range(len(users)):
        if users[ind].id == id:
            users.pop(ind)
            return {'message':'User deleted'}
    raise HTTPException(status_code=404, detail="User not found")