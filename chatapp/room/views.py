from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Message, Room, Reactions


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    for m in messages:
        r = Reactions.objects.filter(messageid=m.id)
        reactions = reactionString(r)

        m.reactions = reactions

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


def reactionString(r):
    reactions = ""
    hearts = MyClass("❤️")
    likes = MyClass("👍️")
    for reaction in r:
        if reaction.reaction == "heart":
            hearts.count += 1
        if reaction.reaction == "like":
            likes.count += 1

    for elem in [likes, hearts]:
        if elem.count > 0:
            reactions += f"{elem.count}x{elem.reaction}, "
    return reactions


class MyClass:
    def __init__(self, r):
        self.reaction = r
        self.count = 0
