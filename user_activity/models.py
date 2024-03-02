from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from user.models import BaseModel

User = get_user_model()


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')


class Like(BaseModel):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
     object_id = models.PositiveIntegerField(null=True, blank=True)
     content_object = GenericForeignKey('content_type', 'object_id')
