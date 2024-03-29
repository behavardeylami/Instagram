# Generated by Django 4.2 on 2024-03-02 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('story', models.FileField(upload_to='content/stories/', verbose_name='Story')),
                ('content', models.TextField(blank=True, max_length=100, null=True, verbose_name='Content')),
                ('expires_at', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'Stories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('caption', models.TextField(blank=True, null=True, verbose_name='caption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Mention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('post_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mentions', to='content.post')),
                ('story_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mentions', to='content.story')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentions_sent', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentions_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mention',
                'verbose_name_plural': 'Mentions',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('file', models.FileField(upload_to='content/media/', verbose_name='File')),
                ('media_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video')], default='image', max_length=10, verbose_name='Media type')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Medias',
            },
        ),
    ]
