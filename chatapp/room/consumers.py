import json
from channels.generic.websocket import AsyncWebsocketConsumer
# Slouží k ukládání do databáze v asynchronním pohledu
from asgiref.sync import sync_to_async

from django.contrib.auth.models import User

from .models import Message, Room, Reactions
from .views import reactionString


# Připojení a odpojení do chat serveru
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # vytvoření objektu reakce v databázi
    @sync_to_async
    def handlereaction(self, username, room, message, id):
        print(message)
        messagedb = Message.objects.get(id=id)
        Reactions.objects.create(messageid=messagedb, reaction=message)

    async def emitreactions(self, id):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'reaction_update',
                'isreaction': True,
                'messageid': id,
                'reactions': self.getreactionsbymessageid(id),
            }
        )


    async def reaction_update(self, event):
        isreaction = event['isreaction']
        messageid = event['messageid']
        reactions = event['reactions']
        await self.send(text_data=json.dumps({
            'isreaction': isreaction,
            'messageid': messageid,
            'reactions': reactions,
        }))

    # získání reakce podle id konkrétní zprávy
    @sync_to_async
    def getreactionsbymessageid(self, messageid):
        reactions = Reactions.objects.filter(messageid=messageid)[0:50]
        print('reakce', reactionString(reactions))
        return reactionString(reactions)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        if data["isreaction"]:
            id = data["id"]
            await self.handlereaction(username, room, message, id)
            all_reactions = await self.getreactionsbymessageid(id)


            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'reaction_update',
                    'isreaction': True,
                    'messageid': id,
                    'reactions': all_reactions,
                }
            )
        else:
            id = await self.save_message(username, room, message)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'room': room,
                    'id': id
                }
            )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']
        id = event['id']
        print("xddd", event)
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room,
            'id': id
        }))

    # ukládání zprávy
    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        xd = Message.objects.create(user=user, room=room, content=message)
        return xd.id
