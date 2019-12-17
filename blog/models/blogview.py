from django.contrib.auth.models import User
from django.db import models
from blog.models.post import Post
class BlogView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # current user id's
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # whose blogs we viewed
