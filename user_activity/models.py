from django.db import models
from content.models import Post
# from django.db.models.signals import post_save, post_delete
from django.contrib.auth import get_user_model
from user.models import BaseModel

User = get_user_model()


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def user_comment_post(sender, instance, *args, **kwargs):
            comment = instance
            post = comment.post
            text_preview = comment.body[:90]
            sender = comment.user

    def user_del_comment_post(sender, instance, *args, **kwargs):
            like = instance
            post = like.post
            sender = like.user

            notify = Notification.objects.filter(post=post, sender=sender, notification_type=2)
            notify.delete()

# post_save.connect(Comment.user_comment_post, sender=Comment)
# post_delete.connect(Comment.user_del_comment_post, sender=Comment)


class Likes(BaseModel):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')

	def user_liked_post(sender, instance, *args, **kwargs):
		like = instance
		post = like.post
		sender = like.user

	def user_unlike_post(sender, instance, *args, **kwargs):
		like = instance
		post = like.post
		sender = like.user

# post_save.connect(Likes.user_liked_post, sender=Likes)
# post_delete.connect(Likes.user_unlike_post, sender=Likes)