from django.urls import path
from .views import HomePageView, AlbumDetailView

urlpatterns = [
    path("<int:pk>", AlbumDetailView.as_view(), name="album_detail"),
    path("", HomePageView.as_view(), name="album_list")
]
