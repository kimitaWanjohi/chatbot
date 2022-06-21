import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from bot.openai.main import init_chat

class ChatBotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.connect()

    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']

        res = await init_chat(message)

        