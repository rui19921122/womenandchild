from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class CustomUser(models.Model):
    phone = models.CharField(max_length=12, verbose_name='电话号码', blank=True)
    user = models.OneToOneField(User, verbose_name='用户', editable=False)
    sex = models.CharField(max_length=1, verbose_name='性别', choices=(('m', '男'), ('f', '女')))
    birth_day = models.DateField(verbose_name='生日', blank=True)
    name = models.CharField(max_length=10, verbose_name='姓名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '姓名'
