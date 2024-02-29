from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    is_active = models.BooleanField(verbose_name="Is active", default=True)
    created_at = models.DateTimeField(verbose_name="Date created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date updated", auto_now=True)
    
    
    class Meta:
        abstract = True
        ordering = ("pk",)


    def __str__(self):
        raise NotImplementedError("Implement __str__ method")
    

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    username = models.CharField(max_length=30, null=False, blank=False, verbose_name='Username')
    public = models.BooleanField(null=False, blank=False, default=False, verbose_name='public')
    profile_picture = models.ImageField(upload_to='user/profiles/', null=True, blank=True, verbose_name='profilepicture')
    bio = models.TextField(max_length=500, null=True, blank=True)
    following = models.ManyToManyField(User, blank=True, related_name='followers')
    followers = models.ManyToManyField(User, blank=True, related_name='following')

    class Meta:
        verbose_name = 'Instauser'
        verbose_name_plural = 'Instausers'

    def __str__(self):
        return str(self.user)

    def save_profile(self):
        self.save()
    
    def update_profile(self):
        self.update()
    
    def delete_profile(self):
        self.delete()
  
    @classmethod
    def search_user(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
