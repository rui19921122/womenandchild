# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='model',
            field=models.ForeignKey(default=1, to='news.Models', verbose_name='板块名称'),
            preserve_default=False,
        ),
    ]
