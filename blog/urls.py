from django.urls import path
from blog.views.comment import CommentCreate
from blog.views.home import home
from blog.views.post import PostView, PostCreate
from blog.views.like import LikeButton
from blog.views.dislike import DisLikeButton
from blog.views.dashboardview import dashboardhome,mostcommented,mostliked,mostviewed,searchblog
app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    path('', home, name='home'),
    # ex: /blog/ravi
    path('<str:username>/', dashboardhome, name='user_posts'),
    # ex: /blog/postcomments/ravi/merum
    path('postcomments/<str:username>/<str:comments>',mostcommented,name='mostcommented'),
    # ex: /blog/postlikes/ravi/merum
    path('postlikes/<str:username>/<str:comments>',mostliked,name='mostliked'),
    # ex: /blog/postviews/ravi/merum
    path('postviews/<str:username>/<str:comments>',mostviewed,name='mostviewed'),
    # ex: /blog/postsearch/ravi/?search_box=Something
    path('postsearch/<str:username>/',searchblog,name='searchblog'),
    # ex: /blog/post/5/
    path('post/<int:pk>/', PostView.as_view(), name='post'),
    # ex: /blog/post/create/
    path('post/create/', PostCreate.as_view(), name='create_post'),
    # ex: /blog/post/12/comment/
    path('post/<int:pk>/comment/', CommentCreate.as_view(), name='create_comment'),
    # ex: /blog/post/11/it will redirect same page
    path('like/<int:username>/<str:title>/',LikeButton,name='like_button'),
    # ex: /blog/post/11/it will redirect same page
    path('dislike/<int:username>/<str:title>/',DisLikeButton,name='dislike_button'),
]
