from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings
<<<<<<< HEAD
from django.db.models import ImageField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# from .utils import edit_photo
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
=======
>>>>>>> 02ac08a5e02b8c2bb1451d42ec17bf3afa8b0827

# Create your models here.


<<<<<<< HEAD

class Messages(models.Model):
    pic = ProcessedImageField(upload_to='message/posts',
                              null=True, blank=True,
                              processors=[ResizeToFill(500, 150)],
                              format='JPEG',
                              options={'quality': 60})

    editedpic = ImageField(upload_to='message/edit',null=True, blank=True,)
=======
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
>>>>>>> 02ac08a5e02b8c2bb1451d42ec17bf3afa8b0827
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
<<<<<<< HEAD
    )
=======
    )
>>>>>>> 02ac08a5e02b8c2bb1451d42ec17bf3afa8b0827
