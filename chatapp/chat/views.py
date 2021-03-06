from django.shortcuts import render, redirect
from chat.models import Room, Message

# Create your views here.
def index(request):
    return render(request,'chat/index.html')


def room(request,room):
    if request.method == 'POST':
        pass

    return render(request,'chat/room.html')


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    print(room)
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)