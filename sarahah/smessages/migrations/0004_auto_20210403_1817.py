# Generated by Django 3.0.8 on 2021-04-03 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smessages', '0003_auto_20210403_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='image',
            new_name='pic',
        ),
    ]
