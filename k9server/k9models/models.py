from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    message_text = models.TextField(default="")
    recv_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True)