from django.db import models
from django.contrib.auth import get_user_model
from user.models import BaseModel

User = get_user_model()


class Post(BaseModel):
    pass


class Media(BaseModel):
    pass


class Mentons(BaseModel):
    pass


class Tag(BaseModel):
    pass