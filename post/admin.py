from django.contrib import admin
from .models import Post, Tags
from django.utils.safestring import mark_safe


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'get_image')
    save_on_top = True
    list_filter = ('title',)
    search_fields = ('title', 'tags')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width=50px height=50px')

    get_image.short_description = 'Изображение'


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    save_on_top = True
    list_filter = ('url_tags',)
    search_fields = ('title',)


admin.site.site_title = 'Обработка контента'
admin.site.site_header = 'Обработка контента'
