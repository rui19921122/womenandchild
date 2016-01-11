# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20151118_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsChild',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='大板块名称', max_length=10)),
                ('number', models.SmallIntegerField(verbose_name='排序')),
            ],
            options={
                'ordering': ['-number'],
                'verbose_name': '子版块',
            },
        ),
        migrations.CreateModel(
            name='ModelsParent',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='大板块名称', max_length=10)),
                ('number', models.SmallIntegerField(verbose_name='排序')),
            ],
            options={
                'ordering': ['-number'],
                'verbose_name': '父板块',
            },
        ),
        migrations.AlterField(
            model_name='picture',
            name='pic',
            field=models.ImageField(upload_to='upload'),
        ),
        migrations.AddField(
            model_name='modelschild',
            name='parent',
            field=models.ForeignKey(verbose_name='父板块', to='news.ModelsParent'),
        ),
    ]
