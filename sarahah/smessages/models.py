from PIL import ImageDraw
from PIL import Image
from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings
from django.db.models import ImageField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from .utils import edit_photo, compressImage


# Create your models here.
# class MessagesManager(models.Manager):
#     def edit_photo(self):
#
#         # m = Messages.objects.all()
#         # for i in m :
#         #     print(i.pic)
#         url = self.pic
#         im = Image.open(self.pic)
#         # print(im)
#         img_draw = ImageDraw.Draw(im)
#         img_draw.text((70, 250), 'Hello World', fill='white')
#         im.save("message/edit/{url}".format(url=im))
#         print("message/edit/{url}".format(url=im))
#         print(self.pk)
#         self.editedpic = im
#         print(self.editedpic.url)
#         self.save()
#         # print(pk)

class Messages(models.Model):
    pic = ProcessedImageField(upload_to='message/posts',
                              null=True, blank=True,
                              processors=[ResizeToFill(400, 400)],
                              format='JPEG',
                              options={'quality': 60})

    editpic = ProcessedImageField(upload_to='message/edit',
                                  null=True, blank=True,
                                  processors=[ResizeToFill(400, 400)],
                                  format='JPEG',
                                  options={'quality': 60})

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
    notreport = models.BooleanField(
        'Not reported', default=True
    )

    # def __init__(self):
    #     for a in self.objects.all():
    #         edit_photo(a)
    def save(self, *args, **kwargs):
        if self.favorite == True:
            super().save(*args, **kwargs)
        else:
            self.pic = compressImage(self.pic)
            super().save(*args, **kwargs)
            self.editpic = edit_photo(self.pic, self.received)

            super().save(*args, **kwargs)


class report(models.Model):
    mess = models.ForeignKey(Messages, on_delete=models.CASCADE, related_name='reported_message')
