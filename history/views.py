from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Artist, Song
from .forms import ArtistForm, SongForm
from django.db import connection

# Create your views here.

def index(request):
    '''display a list of artists'''

    artists = Artist.objects.raw('SELECT * FROM history_artist')
    print("raw artist", artists)
    context = {'artists': artists}
    return render(request,'history/index.html', context)

def detail(request, artist_id):
    '''the artist detail page'''

    sql = '''
        SELECT * FROM history_artist
        WHERE id=%s
        '''
    artist = Artist.objects.raw(sql,[artist_id])[0]
    print('selected artist', artist)
    context = {'artist': artist}
    return render(request, 'history/artist_detail.html', context)

def new_artist(request):
    '''add a new artist'''

    if request.method == 'GET':
        artists = Artist.objects.raw('SELECT * FROM history_artist')
        context = {
            'route': 'history:new_artist',
            'artists': artists
        }
        return render(request, 'history/new_artist.html', context)
    
    if request.method == 'POST':
        name = request.POST['name']

        with connection.cursor() as cursor:
            cursor.execute('INSERT into history_artist VALUES(%s,%s)', [None,name])
            new_artist_id = cursor.lastrowid
            print("new artist id", new_artist_id)

            return HttpResponseRedirect(reverse('history:index'))

