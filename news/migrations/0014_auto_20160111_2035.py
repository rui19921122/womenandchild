# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20160111_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpic',
            name='name',
            field=models.CharField(max_length=50, verbose_name='好记的名称', default='首页图片'),
        ),
        migrations.AlterField(
            model_name='mainpic',
            name='url',
            field=models.URLField(help_text='请输入点击图片或链接后的跳转地址，为空则跳转首页', blank=True, verbose_name='指向'),
        ),
    ]
