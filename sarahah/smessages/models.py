from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings

# Create your models here.


class Messages(models.Model):
    message = models.CharField(
        'Message',
        max_length=255,
        help_text="You have 255 characters remaining",
        blank=True
    )

    pic = models.ImageField(
        upload_to='message/posts', verbose_name='Picture ',
        null=True, blank=True)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="User sender",
        related_name='sender'
    )

    received = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="User received",
        related_name='received'
    )

    date_joined = models.DateTimeField('Post Date', auto_now_add=True)

    favorite = models.BooleanField(
        'Favorite', default=False
    )