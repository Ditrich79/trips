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
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_admin_photo', 'picture1', 'get_admin_pictures1',
              'picture2', 'get_admin_pictures2', 'picture3', 'get_admin_pictures3', 'picture4', 'get_admin_pictures4',
              'picture5', 'get_admin_pictures5', 'is_published', 'time_created', 'time_update')
    readonly_fields = ('get_admin_photo', 'time_created', 'time_update', 'get_admin_pictures1', 'get_admin_pictures2',
                       'get_admin_pictures3', 'get_admin_pictures4', 'get_admin_pictures5')
    save_on_top = True

    def get_html_photo(self, item):
        if item.photo:
            return mark_safe(f"<img src='{item.photo.url}' width='60'>")

    def get_admin_photo(self, item):
        if item.photo:
            return mark_safe(f"<img src='{item.photo.url}' width='200'>")

    def get_admin_pictures1(self, item):
        if item.picture1:
            return mark_safe(f"<img src='{item.picture1.url}' width='200'>")

    def get_admin_pictures2(self, item):
        if item.picture2:
            return mark_safe(f"<img src='{item.picture2.url}' width='200'>")

    def get_admin_pictures3(self, item):
        if item.picture3:
            return mark_safe(f"<img src='{item.picture3.url}' width='200'>")

    def get_admin_pictures4(self, item):
        if item.picture4:
            return mark_safe(f"<img src='{item.picture4.url}' width='200'>")

    def get_admin_pictures5(self, item):
        if item.picture5:
            return mark_safe(f"<img src='{item.picture5.url}' width='200'>")

    get_html_photo.short_description = 'Фотография'
    get_admin_photo.short_description = 'Главная фотография'
    get_admin_pictures1.short_description = 'Фотография слайдера 1'
    get_admin_pictures2.short_description = 'Фотография слайдера 2'
    get_admin_pictures3.short_description = 'Фотография слайдера 3'
    get_admin_pictures4.short_description = 'Фотография слайдера 4'
    get_admin_pictures5.short_description = 'Фотография слайдера 5'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = 'Административная панель сайта "Любитель путешествий"'
admin.site.site_title = 'Административная панель сайта "Любитель путешествий"'
