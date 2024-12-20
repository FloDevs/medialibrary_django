from django.shortcuts import render
from admin_app.models.board_game_model import BoardGame  
from admin_app.models.cd_model import Cd
from admin_app.models.book_model import Book
from admin_app.models.dvd_model import Dvd
from itertools import chain  


def list_media(request):
    medias = chain(BoardGame.objects.all(), Cd.objects.all(), Book.objects.all(), Dvd.objects.all())
    return render(request, 'member_app/media_list.html', {'medias': medias})

