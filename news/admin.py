from django.contrib import admin

from news.models import Article, Comment, Models, Picture, MainPic, SecondaryPic


# Register your models here.
@admin.register(Article, Comment, Models, Picture, MainPic, SecondaryPic)
class ArticleAdmin(admin.ModelAdmin):
    pass
