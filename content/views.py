from rest_framework import generics
from .models import Post, Story
from .serializers import PostSerializer, StorySerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class StoryListAPIView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class StoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
