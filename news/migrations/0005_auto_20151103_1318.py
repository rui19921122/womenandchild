# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20151103_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='create_people',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
