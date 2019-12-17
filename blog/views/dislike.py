from blog.models.dislike import DisLikeModel
from blog.models.like import LikeModel
from blog.models.post import Post
from django.shortcuts import redirect
def DisLikeButton(self,username,title):
    p=str(self.META.get('HTTP_REFERER'))
    if DisLikeModel.objects.filter(user_id=self.user.id,post_id=username):
        a = LikeModel.objects.filter(user_id=self.user.id, post_id=username)
        a.delete()
    else:
        DisLikeModel.objects.create(user=self.user,post=Post.objects.get(id=username))
        a = LikeModel.objects.filter(user_id=self.user.id, post_id=username)
        a.delete()
    return redirect(p[21:])