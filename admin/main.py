from fastapi import FastAPI
from sqladmin import Admin, ModelView
from base import async_engine
from models import Message

app = FastAPI()
admin = Admin(app, engine=async_engine)


class MessageAdmin(ModelView, model=Message):
    column_list = Message().getall()


admin.add_view(MessageAdmin)
