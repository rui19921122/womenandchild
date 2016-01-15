from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
from xpinyin import Pinyin


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=20, verbose_name='新闻标题')
    create_time = models.DateTimeField(auto_now_add=True)
    color = models.CharField(choices=(('black', '黑色'), ('white', '白色')), default='black', max_length=15,
                             help_text='''定义文字在首页显示的颜色''', verbose_name='首页文字颜色')
    content = RichTextField(verbose_name='新闻内容')
    model = models.ForeignKey('news.Models', verbose_name='过渡板块名称')
    main_model = models.ForeignKey('news.ModelsChild', verbose_name='板块名称', null=True)
    view_count = models.IntegerField(verbose_name='访问数', default=0, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '在这里编辑文章'
        ordering = ['-create_time', ]


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, verbose_name='评论人')
    create_time = models.DateField(auto_now_add=True)
    content = models.TextField(verbose_name='评论内容')
    news = models.ForeignKey('news.Article')
    checked = models.BooleanField(verbose_name='是否已检查', default=False)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

    def __str__(self):
        return self.content


class MainPic(models.Model):
    url = models.URLField(verbose_name='指向', help_text='请输入点击图片或链接后的跳转地址，为空则不跳转', blank=True)
    pic = ProcessedImageField(upload_to='index', verbose_name='首页图片,建议为2000*500分辨率', processors=[ResizeToFill(
            width=2000, height=550)], format='JPEG', options={'quality': 95})
    upload_date = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)
    on_home = models.NullBooleanField(default=True, verbose_name='是否在首页显示',
                                      help_text='图片是否在首页显示，如果觉得首页显示图片过多，请把其他不需要首页显示的条目此项去掉')
    name = models.CharField(verbose_name='好记的名称', default='首页图片', max_length=50)

    class Meta:
        verbose_name = '首页大图'
        ordering = ['-upload_date']

    def __str__(self):
        return self.name


class SecondaryPic(models.Model):
    url = models.URLField(verbose_name='指向', help_text='请输入点击图片或链接后的跳转地址，为空则不跳转', blank=True)
    title = models.CharField(verbose_name='标题', max_length=30)
    text = models.CharField(verbose_name='文本', max_length=100)
    pic = models.ImageField(upload_to='index', verbose_name='图片')
    # pic = ProcessedImageField(upload_to='index', verbose_name='图片,建议为460*320分辨率', processors=[ResizeToFill(
    #         width=460, height=320)], format='JPEG', options={'quality': 95})
    upload_date = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)

    class Meta:
        verbose_name = '次要首页图片'
        ordering = ['-upload_date']

    def __str__(self):
        return self.title


class Picture(models.Model):
    pic = ProcessedImageField(upload_to='upload', processors=[ResizeToFit(700)], format='JPEG',
                              options={'quality': 95},
                              )
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
    name = models.CharField(max_length=10, verbose_name='子板块名称')
    parent = models.ForeignKey('news.ModelsParent', verbose_name='父板块')
    number = models.SmallIntegerField(verbose_name='排序')
    shortcut = models.CharField(max_length=100, verbose_name='简写', editable=False, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if len(self.name) > 0:
            self.shortcut = Pinyin().get_pinyin(self.name, '')[:30]
            super(ModelsChild, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-number']
        verbose_name = '子版块'
