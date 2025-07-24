from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    type = models.CharField(max_length=50)

class Rating(models.Model):
    type = models.CharField(max_length=50)

class Director(models.Model):
    name = models.CharField(max_length=100)

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movies(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="posters/")
    DateOfRelease = models.DateField()
    RottenTomatoes = models.IntegerField()
    BoxOfficeCollection = models.BigIntegerField()
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)  
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

class Comment(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = CKEditor5Field('Text', config_name='extends')
    timestamp = models.DateTimeField(auto_now_add=True)  

    

