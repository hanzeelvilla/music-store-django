from django.views.generic import ListView, DetailView
from .models import Album

class HomePageView(ListView):
    model = Album
    template_name = "home.html"
    
class AlbumDetailView(DetailView):
    model = Album
    template_name = "album_detail.html"