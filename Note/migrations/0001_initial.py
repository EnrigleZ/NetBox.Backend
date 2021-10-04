# Generated by Django 3.0.5 on 2021-09-25 17:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('title', models.CharField(default='', max_length=120, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('image_ids', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='createTime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updateTime')),
            ],
        ),
    ]