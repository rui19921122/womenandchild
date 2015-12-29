# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20151103_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='color',
            field=models.CharField(choices=[('black', '黑色'), ('white', '白色')], default='black', max_length=15),
        ),
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(to='news.Article'),
        ),
    ]
