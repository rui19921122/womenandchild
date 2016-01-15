from django.contrib import admin

from news.models import Article, Comment, Models, Picture, MainPic, SecondaryPic, ModelsParent, ModelsChild


# Register your models here.
@admin.register(Article, Comment, Models, Picture, MainPic, SecondaryPic, ModelsParent, ModelsChild)
class ArticleAdmin(admin.ModelAdmin):
    pass
