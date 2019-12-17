from django.contrib import admin

from blog.models.comment import Comment
from blog.models.post import Post
from blog.models.like import LikeModel
from blog.models.dislike import DisLikeModel
from blog.models.blogview import BlogView
# Registering every model class in admin interface
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(LikeModel)
admin.site.register(DisLikeModel)
admin.site.register(BlogView)