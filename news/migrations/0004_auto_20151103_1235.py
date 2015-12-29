# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pic',
            field=models.ImageField(null=True, upload_to='', verbose_name='首页图片', default=None),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='models',
            name='order',
            field=models.SmallIntegerField(help_text='决定板块在banner的顺序，如前方比此数字小的板块数多于4个，将被折叠进二级标题', verbose_name='首页排序', unique=True),
        ),
    ]
