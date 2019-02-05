from django import forms


class ArtistForm(forms.Form):
    '''Form for adding a new artist'''

    artist_name = forms.CharField(label='Artist Name', max_length=100)

class SongForm(forms.Form):
    '''Form for adding a new song'''

    song_name = forms.CharField(label='Song Name', max_length=100)