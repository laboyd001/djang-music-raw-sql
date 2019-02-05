from django.urls import path
from . import views

app_name = 'history'
urlpatterns = [
    # display all the artist names
    path('', views.index, name='index'),
    path('detail/<int:artist_id>/', views.detail, name='detail'),
    path('new_artist/', views.new_artist, name='new_artist'),
]