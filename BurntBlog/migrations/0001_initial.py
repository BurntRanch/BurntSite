# Generated by Django 5.2.1 on 2025-06-03 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('uid', models.UUIDField(primary_key=True, serialize=False, unique=True, verbose_name='Post UUID')),
                ('Post Title', models.CharField(verbose_name='The title of this post.')),
                ('Post Content', models.TextField(verbose_name='The content of this post.')),
                ('Date', models.DateTimeField(auto_now=True, verbose_name='Date of publishing.')),
            ],
        ),
    ]
