# Generated by Django 3.0.8 on 2021-04-03 17:08

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('smessages', '0006_remove_messages_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='pic',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='message/posts'),
        ),
    ]
