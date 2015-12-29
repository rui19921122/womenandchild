# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='板块名称', max_length=8)),
                ('is_important', models.BooleanField(default=False, verbose_name='首页显示', help_text='板块是否需要在首页中显示')),
                ('order', models.SmallIntegerField(verbose_name='首页排序', help_text='决定板块在banner的顺序，如前方比此数字小的板块数多于4个，将被折叠进二级标题')),
            ],
        ),
    ]
