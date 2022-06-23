from bot.openai.main import init_chat
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

@shared_task
def broker(prompt):
    res = init_chat(prompt=prompt)

    channel_layer.send()
