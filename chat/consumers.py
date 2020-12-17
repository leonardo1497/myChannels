import json 
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


from django.utils import timezone, dateformat

class ChatCosumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.id
        self.user = self.scope['user']
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type' : 'chat_message',
                'message' : message,
                'username' : self.user.username,
                'datetime': dateformat.format(timezone.now(),'Y-m-d H:i:s')
            },
        )

    async def chat_message(self, event):
        message = event['message']
        datetime = event['datetime']
        username = event['username']
        await self.send(text_data=json.dumps({'message': message, 'username' : username, 'datetime': datetime}))