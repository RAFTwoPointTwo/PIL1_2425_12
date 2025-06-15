#consumers

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
'''from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.recipient_email = self.scope['url_route']['kwargs']['recipient_email']
        self.user = self.scope['user']

        if not self.user.is_authenticated:
            await self.close()
            return

        self.room_name = f"chat_{min(self.user.email, self.recipient_email)}_{max(self.user.email, self.recipient_email)}"
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_email = text_data_json['sender']
        recipient_email = text_data_json['receiver']

        sender = await sync_to_async(User.objects.get)(email=sender_email)
        recipient = await sync_to_async(User.objects.get)(email=recipient_email)

        # Sauvegarder le message en base de données
        await sync_to_async(Message.objects.create)(
            sender=sender,
            receiver=recipient,
            content=message
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender_email,
                'timestamp': str(datetime.now())
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        timestamp = event['timestamp']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'timestamp': timestamp
        }))'''

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender = data['sender']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']


        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))
