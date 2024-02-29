from django.db import models
from django.db.models import Max
from django.contrib.auth import get_user_model
from user.models import BaseModel

User = get_user_model()


class Message(BaseModel):
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
        sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
        recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
        text = models.TextField(max_length=1000, blank=True, null=True)
        image = models.ImageField(upload_to='direct/message_images/', blank=True, null=True)
        video = models.FileField(upload_to='direct/message_videos/', blank=True, null=True)
        voice = models.FileField(upload_to='direct/message_voices/', blank=True, null=True)
        date = models.DateTimeField(auto_now_add=True)
        is_read = models.BooleanField(default=False)

        def send_message(from_user, to_user, text, image=None, video=None, voice=None):
            sender_message = Message(user=from_user, sender=from_user, recipient=to_user, text=text, is_read=True)
            if image:
                sender_message.image = image
            if video:
                sender_message.video = video
            if voice:
                sender_message.voice = voice

            sender_message.save()

            recipient_message = Message(user=to_user, sender=from_user, text=text, recipient=from_user,)
            if image:
                recipient_message.image = image
            if video:
                recipient_message.video = video
            if voice:
                recipient_message.voice = voice

            recipient_message.save()
            return sender_message

        def get_messages(user):
            messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
            users = []
            for message in messages:
                users.append({
                    'user': User.objects.get(pk=message['recipient']),
                    'last': message['last'],
                    'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
                    })
            return users
