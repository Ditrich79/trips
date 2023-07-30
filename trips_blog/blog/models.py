from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фотография')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    picture1 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True, verbose_name='Картинка1')
    picture2 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True, verbose_name='Картинка2')
    picture3 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True, verbose_name='Картинка3')
    picture4 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True, verbose_name='Картинка4')
    picture5 = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True, verbose_name='Картинка5')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})

    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_created']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
