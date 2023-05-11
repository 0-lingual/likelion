from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    user_password = models.IntegerField()
    user_name = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()


