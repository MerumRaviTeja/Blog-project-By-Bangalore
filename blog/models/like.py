from django.db import models
from blog.models.post import Post
from django.contrib.auth.models import User

class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # current user
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # whose blogs we liked
