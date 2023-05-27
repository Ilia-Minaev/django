from django.contrib import admin
from .models import News, Category

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'created_at',
                    'updated_at',
                    'is_published',
                    'category',
                    'get_photo')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'category')
    fields = ('title',
              'content',
              'photo',
              'get_photo',
              'is_published',
              'views',
              'created_at',
              'updated_at', )
    readonly_fields = ('get_photo',
                       'views',
                       'created_at',
                       'updated_at',)
    save_on_top = False

    def get_photo(self, obj):
        from django.utils.safestring import mark_safe
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="width: 70px;">')
        else:
            return mark_safe(f'<div style="color:red">No photo</div>')

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
