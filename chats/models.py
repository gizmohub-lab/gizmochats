from django.db import models
from django.contrib.auth.models import User

class chats(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    texts = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='chat_files/', blank=True, null=True)
    file = models.FileField(upload_to='chat_files/', blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} : {self.texts[:20]}"