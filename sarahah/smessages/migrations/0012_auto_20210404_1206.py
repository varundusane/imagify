# Generated by Django 3.1.4 on 2021-04-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smessages', '0011_editedmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editedmessage',
            name='editpic',
        ),
        migrations.AddField(
            model_name='messages',
            name='editpic',
            field=models.ImageField(blank=True, null=True, upload_to='message/edit'),
        ),
    ]