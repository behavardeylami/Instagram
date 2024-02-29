from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from user.models import BaseModel
User = get_user_model()
class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_owner')
    caption = models.TextField(null=True, blank=True, verbose_name='caption')
    posted = models.DateTimeField(auto_now_add=True)
    class Meta:
           verbose_name = 'Post'
           verbose_name_plural = 'Posts'
    def __str__(self):
           return self.caption
    def get_absolute_url(self):
           return reverse('postdetails', args=[str(self.id)])
class Media(BaseModel):
    MEDIA_TYPE = (
        ("image", "Image"),
        ("video", "Video"),
    )
    file = models.FileField(upload_to='content/media/', verbose_name='File')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE, default="image", null=False, blank=False, verbose_name='Media type')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post', related_name='Medias')
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'
    def __str__(self):
        return f'{self.date} - {self.post}'
class story(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_owner')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = self.created_at + timezone.timedelta(hours=24)
        super().save(*args, **kwargs)
class Mentons(BaseModel):
    pass
class Tag(BaseModel):
    title = models.CharField(max_length=75, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True)
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

