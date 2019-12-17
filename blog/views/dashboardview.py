from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models.post import Post
from django.db.models import Count
NUM_OF_POSTS = 5

# this func shows dashboard
def dashboardhome(request, username=None):
    user = User.objects.get(username=username)
    first_name = user.first_name
    last_name = user.last_name
    post_list = Post.objects.filter(user=user)
    post_list = post_list.order_by('-pub_date')
    paginator = Paginator(post_list, NUM_OF_POSTS)  # Show NUM_OF_PAGES posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/dashboard.html', {'posts': posts,
                                              'first_name': first_name,
                                              'last_name': last_name})

# this func returns most commented blogs
def mostcommented(request,username,comments):
    user = User.objects.get(username=username)
    id=user.id
    comment=Post.objects.filter(user=id).annotate(num_comments=Count('comments')).order_by('-num_comments')
    return render(request,'blog/most_commented.html',{'comment':comment})

# this func returns most liked blogs
def mostliked(request,username,comments):
    user = User.objects.get(username=username)
    id=user.id
    liked=Post.objects.filter(user=id).annotate(num_likes=Count('likemodel')).order_by('-num_likes')
    return render(request,'blog/most_liked.html',{'liked':liked})

# this func returns most viewed blogs
def mostviewed(request,username,comments):
    user = User.objects.get(username=username)
    id=user.id
    viewed=Post.objects.filter(user=id).annotate(num_views=Count('blogview')).order_by('-num_views')
    return render(request,'blog/most_viewed.html',{'viewed':viewed})

# this func returns seach blog details who likes,comments,dislikes
def searchblog(request,username):
        search_query = request.GET.get('search_box', "None")
        blog_id=Post.objects.filter(title__icontains=search_query,user_id=request.user.id)
        return render(request,'blog/searchblogs.html',{'blog_id':blog_id})




