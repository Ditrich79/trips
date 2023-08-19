from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.safestring import mark_safe


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'cat', 'time_created', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_admin_photo', 'picture1', 'picture2', 'picture3',
              'picture4', 'picture5', 'is_published', 'time_created', 'time_update')
    readonly_fields = ('get_admin_photo', 'time_created', 'time_update')
    save_on_top = True

    def get_html_photo(self, item):
        if item.photo:
            return mark_safe(f"<img src='{item.photo.url}' width='60'>")

    def get_admin_photo(self, item):
        if item.photo:
            return mark_safe(f"<img src='{item.photo.url}' width='200'>")

    get_html_photo.short_description = 'Фотография'
    get_admin_photo.short_description = 'Главная фотография'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = 'Административная панель сайта "Любитель путешествий"'
admin.site.site_title = 'Административная панель сайта "Любитель путешествий"'
