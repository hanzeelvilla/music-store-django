from django.views.generic import ListView
from .models import Album

class HomePageView(ListView):
    model = Album
    template_name = "home.html"