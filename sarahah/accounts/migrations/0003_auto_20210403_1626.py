# Generated by Django 3.0.8 on 2021-04-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, verbose_name='Está Ativo?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False, verbose_name='É da Equipe?'),
        ),
    ]
