# Generated by Django 3.0.8 on 2021-04-03 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smessages', '0005_auto_20210403_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='message',
        ),
    ]
