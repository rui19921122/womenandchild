# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20160111_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondaryPic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name='指向', blank=True, help_text='请输入点击图片或链接后的跳转地址，为空则不跳转')),
                ('title', models.CharField(verbose_name='标题', max_length=30)),
                ('text', models.CharField(verbose_name='文本', max_length=100)),
                ('pic', imagekit.models.fields.ProcessedImageField(verbose_name='图片,建议为460*320分辨率', upload_to='index')),
                ('upload_date', models.DateTimeField(verbose_name='上传时间', auto_now_add=True)),
            ],
            options={
                'verbose_name': '次要首页图片',
                'ordering': ['-upload_date'],
            },
        ),
        migrations.AlterField(
            model_name='mainpic',
            name='url',
            field=models.URLField(verbose_name='指向', blank=True, help_text='请输入点击图片或链接后的跳转地址，为空则不跳转'),
        ),
    ]
