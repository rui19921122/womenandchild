# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20160111_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpic',
            name='url',
            field=models.URLField(help_text='请输入点击图片或链接后的跳转地址，默认为空', default='/', verbose_name='指向'),
        ),
    ]
