import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import WebsocketConsumer

from bot.openai.main import init_chat

class ChatBotConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        print(message)

        res = init_chat(str(message))  

        self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': 'res'
        }))