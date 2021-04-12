from django.urls import path

from . import views

app_name = "ratings"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('reviews/<int:review_id>/', views.review_detail, name='review_detail'),
    path('<int:movie_id>/rate_movie/', views.rate_movie, name='rate_movie'),
    path('the_rock/', views.rock, name='rock_movies'),
]


