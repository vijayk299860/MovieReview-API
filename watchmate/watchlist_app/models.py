from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=200)
    website = models.URLField(max_length=100)
    def __str__(self):
        return self.name
    
class WatchList(models.Model):
    title = models.CharField(max_length=100)
    stream = models.ForeignKey(StreamPlatform, related_name='watchlist',on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    avg_rating = models.FloatField(default=0)
    number_of_ratings = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)  
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.TextField(max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList,  on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Review for {self.watchlist.title} - Rating: {self.rating}'

# from django.db import models

# # Create your models here.
# class Movie(models.Model):
#     name = models.CharField(max_length=100)
#     director = models.CharField(max_length=100)
#     description = models.TextField(max_length=200)
#     active = models.BooleanField(default=True) #movie released or not
    
#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = 'Movie'
#         verbose_name_plural = 'Movies'
    
    