from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'article_created'
    list_display = ('title', 'article_created', 'article_body')
    list_display_links = ('title',)

admin.site.register(Article, ArticleAdmin)