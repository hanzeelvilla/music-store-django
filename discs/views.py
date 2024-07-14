from django.db.models import Q
from django.views.generic import ListView, DetailView
from .forms import SearchForm
from .models import Album

class HomePageView(ListView):
    model = Album
    template_name = "album_list.html"
    context_object_name = 'album_list'
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Album.objects.filter(
                Q(title__icontains=query) | Q(artist__name__icontains=query) | Q(genres__name__icontains=query)
            ).distinct()
        return Album.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context
    
class AlbumDetailView(DetailView):
    model = Album
    template_name = "album_detail.html"