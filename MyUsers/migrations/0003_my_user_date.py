# Generated by Django 5.1.1 on 2024-10-08 11:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyUsers', '0002_alter_my_user_password_alter_my_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_user',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]