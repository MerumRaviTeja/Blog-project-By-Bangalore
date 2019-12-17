from blog.models.like import LikeModel
from blog.models.dislike import DisLikeModel
from blog.models.post import Post
from django.shortcuts import redirect
def LikeButton(self,username,title):
    p=str(self.META.get('HTTP_REFERER')) # Redirecting previous page

    # if object already present in like model it will stored again
    if LikeModel.objects.filter(user_id=self.user.id,post_id=username):
        # Deleting object instance, so it will store object either like model or dislike model
        a=DisLikeModel.objects.filter(user_id=self.user.id, post_id=username)
        a.delete()
    else:
        # if object not present in like model it will stored
        LikeModel.objects.create(user=self.user,post=Post.objects.get(id=username))
        # again used del object because, we redirect previous template page not calling method again
        a = DisLikeModel.objects.filter(user_id=self.user.id, post_id=username)
        a.delete()
    return redirect(p[21:]) # it will redirect same page
                            # ex: blog/post/15