from django.contrib import admin
from .models import News, Category

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',
                    'updated_at', 'id_published', 'category')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('id_published', )
    list_filter = ('id_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
