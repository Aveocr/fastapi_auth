# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Необходимо создать RESTful API для регистрации, авторизации и управления записями пользователей, используя следующие технологии и инструменты:
#
# Python
# FastAPI
# Redis для хранения данных в NoSQL формате
# PostgreSQL для хранения данных пользователей и их записей
# JWT-токены для проверки авторизации пользователей
# slowapi для ограничения количества запросов
# Docker для контейнеризации приложения (необязательно)
# Функциональность, которую необходимо реализовать:
#
# Регистрация нового пользователя (POST-запрос на /register) 2
# Авторизация пользователя (POST-запрос на /login) 2
# Разлогинивание пользователя (POST-запрос на /logout) 2
# Создание новой записи (POST-запрос на /tasks) 2
# Получение списка всех записей (GET-запрос на /tasks) 2
# Получение конкретной записи (GET-запрос на /tasks/{task_id}) 2
# Изменение записи (PUT-запрос на /tasks/{task_id}) 2
# Удаление записи (DELETE-запрос на /tasks/{task_id}) 2
# Для каждого запроса, кроме регистрации и авторизации, необходимо проверять авторизацию пользователя по JWT-токену.
# Для ограничения количества запросов необходимо использовать slowapi с лимитом 100 запросов в минуту. 4
#
# Для хранения данных пользователей и их записей используется PostgreSQL. Для хранения данных в NoSQL
# формате используется Redis. Все соединения с базами данных должны осуществляться через ORM. 4
#
# Формат ответа должен быть JSON. 2


# fastapi dev main.py
from typing import List, Optional, Union
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

app = FastAPI(
    title="users"
)

fake_task_id = [
    {"task_id": 1, "text": "что-то там 1"},
    {"task_id": 2, "text": "что-то там 2"},
    {"task_id": 3, "text": "что-то там 3"}
]


class Task(BaseModel):
    text: str
    user_id: int


class User(BaseModel):
    id: int
    name: str = Field(max_lenght=100)
    surname: str = Field(max_length=100)
    age: str = Field(ge=6)
    sex: bool
    tasks: Optional[List[Task]]


#     jwd code

@app.post("/register")
async def add_users(users: User):
    return users


@app.post("/login")
async def login(login, password):
    return {
        "login": login,
        "password": password
    }


@app.post("/logout")
async def logout(flag: bool):
    return {
        "response": 200
    }


@app.post("/tasks")
async def add_tasks(text: str, user_id: str):
    return {
        "task_id": None,
        "text": text,
        "user_id": 1
    }


@app.get("/tasks/{task_id}", response_model=List[Task])
async def get_task_id(task_id: int, user_id: int):
    return [task for task in fake_task_id if fake_task_id.get("id") == task_id]


@app.get("/tasks")
async def get_tasks():
    return fake_task_id


# @app.put("/tasks/{task_id}", response_model=Task)
# async def put_task_id(task_id: id, task: Task, access: bool):
#     return Union[200, {
#         fake_task_id[task_id],
#     }, None]


@app.delete("/tasks/{task_id}")
async def delete_task_id(task_id, access: bool):
    if access:
        return {
            "response": 200
        }
    else:
        return {
            "text_error": "not_access"
        }
