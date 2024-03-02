from rest_framework import serializers
from .models import Post, Story, Media, Mention

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class MentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    medias = MediaSerializer(many=True, read_only=True)
    mentions = MentionSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
    medias = MediaSerializer(many=True, read_only=True)
    mentions = MentionSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = '__all__'
