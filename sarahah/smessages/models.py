from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings
from django.db.models import ImageField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# from .utils import edit_photo
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Create your models here.



class Messages(models.Model):
    pic = ProcessedImageField(upload_to='message/posts',
                              null=True, blank=True,
                              processors=[ResizeToFill(500, 150)],
                              format='JPEG',
                              options={'quality': 60})

    editedpic = ImageField(upload_to='message/edit',null=True, blank=True,)
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
