from django.db import models
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from user.models import BaseModel
from user_activity.models import Comment, Like

User = get_user_model()


class Media(BaseModel):
    MEDIA_TYPE = (
        ("image", "Image"),
        ("video", "Video"),
    )
    file = models.FileField(upload_to='content/media/', verbose_name='File')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE, default="image", null=False, blank=False, verbose_name='Media type')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'

    def __str__(self):
        return f'{self.date} - {self.post}'
    

class Mention(BaseModel):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentions_sent')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentions_received')
    post_object = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True, related_name='mentions')
    story_object = models.ForeignKey('Story', on_delete=models.CASCADE, null=True, blank=True, related_name='mentions')
    
    class Meta:
        verbose_name = 'Mention'
        verbose_name_plural = 'Mentions'

    def __str__(self):
        return f'{self.user_from} mentioned {self.user_to} in {self.created_at}'


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_owner')
    caption = models.TextField(null=True, blank=True, verbose_name='caption')
    medias = GenericRelation(Media, related_query_name='post')
    mentions = GenericRelation(Mention, related_query_name='mention_post')
    comments = GenericRelation(Comment, related_query_name='comment_post')
    likes = GenericRelation(Like, related_query_name='like_post')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

  	
    def __str__(self):
           return self.caption       

    def get_absolute_url(self):
           return reverse('postdetails', args=[str(self.id)])


class Story(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_stories')
    content = models.TextField(max_length=100, null=True, blank=True, verbose_name='Content')
    medias = GenericRelation(Media, related_query_name='story')
    mentions = GenericRelation(Mention, related_query_name='mention_story')
    comments = GenericRelation(Comment, related_query_name='comment_story')
    likes = GenericRelation(Like, related_query_name='like_story')
    expires_at = models.DateTimeField()

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __str__(self):
        return self.created_at




# class Tag(BaseModel):
#     title = models.CharField(max_length=75, verbose_name='Tag')
#     slug = models.SlugField(null=False, unique=True)

#     class Meta:
#         verbose_name = 'Tag'
#         verbose_name_plural = 'Tags'

#     def get_absolute_url(self):
# 		return reverse('tags', args=[self.slug])
		
# 	def __str__(self):
# 		return self.title

# 	def save(self, *args, **kwargs):
# 		if not self.slug:
# 			self.slug = slugify(self.title)
# 		return super().save(*args, **kwargs)
