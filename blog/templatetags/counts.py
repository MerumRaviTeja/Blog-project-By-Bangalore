from django import template
from blog.models.comment import Comment
from blog.models.blogview import BlogView
from blog.models.like import LikeModel
from blog.models.dislike import DisLikeModel
register = template.Library()

# this template tag returns views count
@register.filter
def get_viewcount(value):
    view_count=BlogView.objects.filter(post_id=value).count()
    return view_count

# this template tag returns comments count
@register.filter
def get_commentcount(value):
    comment_count = Comment.objects.filter(post_id=value).count()
    return comment_count

# this template tag returns like count
@register.filter
def get_likecount(value):
    like_count = LikeModel.objects.filter(post_id=value).count()
    return like_count

# this template tag returns who views user blog
@register.filter
def get_likes(value):
    likesblog=LikeModel.objects.filter(post_id=value.id)
    return likesblog

# this template tag returns who dislikes user blog
@register.filter
def get_dislikes(value):
    dislikesblog=DisLikeModel.objects.filter(post_id=value.id)
    return dislikesblog

# this template tag returns who comments user blog
@register.filter
def get_comments(value):
    commentsblog=Comment.objects.filter(post_id=value.id)
    return commentsblog