import time
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
#from openai import AsyncOpenAI
from openai import OpenAI

#Необходимые ключи от OpenAI, асисент и тренд
client = OpenAI(api_key='')
assistant_id = ''
thread_id = ''

#Команды для бота
router = Router()

# async def generate_answer(user_message): # для генирации ответа
#     chat_completion = await client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": f"{user_message}",
#             }
#         ],
#         model="gpt-3.5-turbo",
#    )
#     return chat_completion.choices[0].message.content #возвращение результата


def assisten_giper(mes_text):
    # Создание треда сообщений 
    message_create = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=f"{mes_text}"
    )

    # Запуск треда сообщений
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )

    # Задержка крайне обязательна, так как асистенту нужно время, для генерации ответа
    time.sleep(10)

    # Обновление треда
    run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run.id
    )

    # Выводим все сообщения
    messages = client.beta.threads.messages.list(
        thread_id=thread_id,
    )

    # Вывод ответа в терминал, где мы можем его отслеживать
    print(messages.data[0].content[0].text.value)
    # Возвращение ответа пользователю в боте
    return messages.data[0].content[0].text.value



@router.message(CommandStart()) # ответ после сообщения старт
async def cmd_start(message: Message):
    await message.answer(text='К вашим услугам, задайте вопрос!')

@router.message() #будет отвечать на все остальные сообщения
async def gpt_answer(message: Message):
    answer = assisten_giper(message.text) #ответ для пользователя
    await message.answer(f'{answer}') #отправка ответа 


