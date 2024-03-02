from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, StoryListAPIView, StoryDetailAPIView



urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('stories/', StoryListAPIView.as_view(), name='story-list'),
    path('stories/<int:pk>/', StoryDetailAPIView.as_view(), name='story-detail'),
]
