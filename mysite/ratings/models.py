from django.db import models
# from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField('date released')
    has_the_rock = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# these should match the field/names/id's on the html
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    submit_date = models.DateTimeField('date submitted')
    score = models.IntegerField(default=1, 
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    text = models.TextField(blank=True)
    reviewer_name = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.review

    # def review_date(self):
    #     return self.submit_date = datetime.now()