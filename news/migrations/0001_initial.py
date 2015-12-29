# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20, verbose_name='新闻标题')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('content', ckeditor.fields.RichTextField(verbose_name='新闻内容')),
                ('on_home', models.BooleanField(default=False, verbose_name='放在首页？')),
                ('create_people', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('content', models.TextField(verbose_name='新闻内容')),
                ('news', models.ForeignKey(to='news.Article', editable=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pic', models.ImageField(upload_to='')),
            ],
        ),
    ]
