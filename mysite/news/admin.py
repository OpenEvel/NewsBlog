from django.contrib import admin
from .models import *

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    # лист для отображения
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published',)
    # лист ссылок
    list_display_links = ('id', 'title',)
    # по чему поиск
    search_fields = ('title',)
    # какие поля хочу редактировать
    list_editable = ('is_published',)
    # какие поля хочу фильтровать
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    # лист для отображения
    list_display = ('id', 'title',)
    # лист ссылок
    list_display_links = ('id', 'title',)
    # по чему поиск
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
