from django.shortcuts import render, HttpResponse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Create your views here.
def home(request):
    if request.method == 'POST':
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(#client_id= 'your spotify id',client_secret='Your secret key'))
        results = spotify.artist_top_tracks(artist_uri)
        final_result=results['tracks'][:10]
        return render(request, "home.html",{'results':final_result})
    else:    
      return render(request, "home.html")