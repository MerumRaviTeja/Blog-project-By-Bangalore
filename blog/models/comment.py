from django.contrib.auth.models import User
from django.db import models

from blog.models.post import Post


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments') #whose blogs we commented
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

