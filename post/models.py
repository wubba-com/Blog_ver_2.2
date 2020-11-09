from django.db import models
from django.urls import reverse

from django.utils.text import slugify
from time import time


def generation_slug(title):
    """Функция для генерации слага при сохранении конкретного экземпляра класса в БД, но только при создании"""
    new_slug = slugify(title, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Tags(models.Model):
    """Теги к постам"""
    title = models.CharField('Тег', max_length=50)
    url_tags = models.SlugField('url', max_length=50)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.url_tags})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.url_tags})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.url_tags})


class Post(models.Model):
    """Посты"""
    title = models.CharField('Заголовок', max_length=150, db_index=True)
    body_post = models.TextField('Текст', db_index=True)
    image = models.ImageField('Изображение', upload_to='posts/')
    date_publish = models.DateTimeField('Дата публикации', auto_now_add=True)
    url = models.SlugField(max_length=50, unique=True, blank=True)
    tags = models.ManyToManyField(Tags, verbose_name='Тег', blank=True, related_name='posts')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-date_publish']

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.url})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.url})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.url})

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = generation_slug(self.title)
        super().save(*args, **kwargs)
