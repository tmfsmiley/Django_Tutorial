from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Movie, Review
from datetime import datetime

def index(request): 
    list_of_all_movies = Movie.objects.all()[:10]
    context = {'list_of_all_movies': list_of_all_movies}
    return render (request, 'ratings/index.html', context)

def rock(request): 
    list_of_all_movies = Movie.objects.filter(has_the_rock=True)[:10]
    context = {'list_of_all_movies': list_of_all_movies}
    return render (request, 'ratings/index.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'ratings/movie_detail.html', {'movie': movie})

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'ratings/review_detail.html', {'review': review})

# will do this one with Steve
def rate_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    try:
        data = request.POST
        score = data.get('score', 10)
        text = data.get('text', '')
        reviewer_name = data.get('reviewer_name', 'Anonymous')
        submit_date = datetime.now()
        review = Review.objects.create(
            score=score,
            text=text,
            reviewer_name=reviewer_name,
            submit_date=submit_date,
            movie=movie
        )
        return HttpResponseRedirect(reverse('ratings:review_detail', args=(review.id,)))

    except (KeyError):
        pass




