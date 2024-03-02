from django.contrib import admin
from .models import Post, Story, Media, Mention
from user_activity.models import Comment, Like

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'media_type', 'content_object')
    search_fields = ('id', 'media_type', 'content_object__caption')

@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to', 'post_object', 'story_object', 'created_at')
    search_fields = ('user_from__username', 'user_to__username', 'post_object__caption', 'story_object__content')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'created_at')
    search_fields = ('user__username', 'caption')

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'expires_at', 'created_at')
    search_fields = ('user__username', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_post_caption', 'get_story_content', 'created_at')

    def get_post_caption(self, obj):
        return obj.post.caption if obj.post else None

    def get_story_content(self, obj):
        return obj.story.content if obj.story else None

    get_post_caption.short_description = 'Post Caption'
    get_story_content.short_description = 'Story Content'

    search_fields = ('user__username', 'post__caption', 'story__content', 'text')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_post_caption', 'get_story_content', 'created_at')

    def get_post_caption(self, obj):
        return obj.post.caption if obj.post else None

    def get_story_content(self, obj):
        return obj.story.content if obj.story else None

    get_post_caption.short_description = 'Post Caption'
    get_story_content.short_description = 'Story Content'

    search_fields = ('user__username', 'post__caption', 'story__content')
