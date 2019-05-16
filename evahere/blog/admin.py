from django.contrib import admin

# Register your models here.

from .models import Article,Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category','publish_date')


admin.site.register(Article,ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','category_id')


admin.site.register(Category,CategoryAdmin)