from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Параметры'
    )

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группу'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Введите текст поста'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
        help_text='Группа, относительно поста',
        blank=True, null=True)

    class Meta:
        ordering = ['-pub_date', 'author']
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

    def __str__(self):
        return self.text[:15]
