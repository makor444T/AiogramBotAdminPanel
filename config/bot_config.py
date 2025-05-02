import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import dotenv_values

config = dotenv_values("./config/.env.example")
API_TOKEN = config['TOKEN']
ADMIN = int(config['ADMIN'])
USER = config['user']
PASSWORD = config['password']
DB = config['db_name']
HOST = config['host']

CHAT_ID = config['chat_id']

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
