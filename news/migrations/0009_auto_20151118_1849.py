# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20151118_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ip',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
    ]
