# Generated by Django 5.1.4 on 2024-12-19 09:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
