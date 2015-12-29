from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill,ResizeToFit


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=20, verbose_name='新闻标题')
    create_time = models.DateTimeField(auto_now_add=True)
    create_people = models.ForeignKey(User, verbose_name='创建人')
    color = models.CharField(choices=(('black', '黑色'), ('white', '白色')), default='black', max_length=15,
                             help_text='''定义文字在首页显示的颜色''', verbose_name='首页文字颜色')
    content = RichTextField(verbose_name='新闻内容')
    on_home = models.BooleanField(default=False, verbose_name='放在首页？')
    model = models.ForeignKey('news.Models', verbose_name='板块名称')
    pic = models.ImageField(verbose_name='首页图片', blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '在这里编辑文章'
        ordering = ['-create_time', ]


class Comment(models.Model):
    user = models.ForeignKey(User, null=True)
    create_time = models.DateField(auto_now_add=True)
    content = models.TextField(verbose_name='评论内容')
    news = models.ForeignKey('news.Article')
    ip = models.GenericIPAddressField(null=True, blank=True)


class Picture(models.Model):
    pic = models.ImageField(upload_to='upload')
    pic_700 = ImageSpecField(source='pic', processors=[ResizeToFit(700)], format='JPEG', options={'quality': 95})
    name = models.CharField(max_length=50)


class Models(models.Model):
    name = models.CharField(max_length=8, verbose_name='板块名称')
    is_important = models.BooleanField(default=False, help_text='''板块是否需要在首页中显示''', verbose_name='首页显示')
    order = models.SmallIntegerField(verbose_name='首页排序', help_text='决定板块在banner的顺序，如前方比此数字小的板块数多于4个，将被折叠进二级标题',
                                     unique=True)

    def __str__(self):
        return self.name


class ModelsParent(models.Model):
    name = models.CharField(max_length=10, verbose_name='大板块名称')
    number = models.SmallIntegerField(verbose_name='排序')

    class Meta:
        ordering = ['-number']
        verbose_name = '父板块'


class ModelsChild(models.Model):
    name = models.CharField(max_length=10, verbose_name='大板块名称')
    parent = models.ForeignKey('news.ModelsParent', verbose_name='父板块')
    number = models.SmallIntegerField(verbose_name='排序')

    class Meta:
        ordering = ['-number']
        verbose_name = '子版块'
