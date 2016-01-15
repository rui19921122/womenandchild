from django.contrib import admin

from news.models import Article, Comment, Models, Picture, MainPic, SecondaryPic, ModelsParent, ModelsChild


# Register your models here.
@admin.register(Article, Models, Picture, MainPic, SecondaryPic, ModelsParent, ModelsChild)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'news', 'checked')
    list_editable = ('checked',)
    list_filter = ('checked',)
