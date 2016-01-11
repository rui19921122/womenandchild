# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20160111_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPic',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('url', models.URLField(default='#', verbose_name='指向', help_text='请输入点击图片或链接后的跳转地址，默认为空')),
                ('pic', imagekit.models.fields.ProcessedImageField(upload_to='index', verbose_name='首页图片,建议为2000*500分辨率')),
                ('upload_date', models.DateTimeField(verbose_name='上传时间', auto_now_add=True)),
                ('on_home', models.NullBooleanField(verbose_name='是否在首页显示', default=True, help_text='图片是否在首页显示，如果觉得首页显示图片过多，请把其他不需要首页显示的条目此项去掉')),
            ],
            options={
                'ordering': ['-upload_date'],
                'verbose_name': '首页大图',
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论'},
        ),
        migrations.AlterField(
            model_name='picture',
            name='pic',
            field=imagekit.models.fields.ProcessedImageField(upload_to='upload'),
        ),
    ]
