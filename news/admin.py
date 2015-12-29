from django.contrib import admin
from news.models import Article,Comment,Models,Picture


# Register your models here.
@admin.register(Article,Comment,Models,Picture)
class ArticleAdmin(admin.ModelAdmin):
    pass
