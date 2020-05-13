from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    bio = models.CharField(max_length=255)
    avatar = models.CharField(max_length=25)
    password = models.CharField(max_length=255)
    followers = models.ForeignKey('self', on_delete=models.CASCADE)
    account_balance = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # stocks = a list of stocks bought
    # posts = a list of posts uploaded by the user
    # comments = a list of comments uploaded by the user
    # liked_posts = a list of the posts the user liked


class Stock(models.Model):
    symbol = models.CharField(max_length=15)
    price_bought = models.FloatField(default=0.00)
    price_sold = models.FloatField(default=0.00)
    stock_holder = models.ForeignKey(User, related_name="stocks", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    user_who_liked = models.ManyToManyField(User, related_name="liked_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=255)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)