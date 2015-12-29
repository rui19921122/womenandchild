# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20151103_2344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-create_time'], 'verbose_name': '在这里编辑文章'},
        ),
        migrations.AddField(
            model_name='comment',
            name='ip',
            field=models.IPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='color',
            field=models.CharField(choices=[('black', '黑色'), ('white', '白色')], help_text='定义文字在首页显示的颜色', max_length=15, verbose_name='首页文字颜色', default='black'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_people',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pic',
            field=models.ImageField(blank=True, verbose_name='首页图片', upload_to='', default=None),
        ),
    ]
