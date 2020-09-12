from django.urls import path

from .views import MovieList, MovieDetail

app_name = "movies"
urlpatterns = [
    path("", MovieList.as_view(), name="movie_list"),
    path("<uuid:pk>/", MovieDetail.as_view(), name="movie_detail"),
]
