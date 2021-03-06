from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Skill(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    percent = models.IntegerField(verbose_name="Процент", validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return f"{self.name} {self.percent}%"


class Language(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    desc = models.CharField(verbose_name="Описание", max_length=255)
    stars = models.FloatField(verbose_name="Звезды")

    def range_star(self):
        if self.stars % 1 == 0:
            return [1 for _ in range(int(self.stars))]
        else:
            return [1 for _ in range(int(self.stars))] + [0]

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    loc = models.CharField(verbose_name="Учебное заведение", max_length=255)
    year_start = models.IntegerField(verbose_name='Год начала обучения')
    year_end = models.IntegerField(verbose_name='Год окончания обучения')

    class Meta:
        verbose_name = 'Обучение'
        verbose_name_plural = 'Обучение'

    def __str__(self):
        return f"{self.name} {self.year_start}-{self.year_end}"


class SocLink(models.Model):
    CHOICES = [
        ('fa-github', 'GitHub'),
        ('fa-instagram', 'Instagram'),
        ('fa-vk', 'VK'),
    ]

    link = models.URLField(verbose_name="Ссылка", max_length=255)
    class_name = models.CharField(verbose_name="Соц. Сеть", max_length=255, choices=CHOICES)
    sort = models.IntegerField(verbose_name='Сортировка', default=100)

    class Meta:
        verbose_name = 'Соц. сеть'
        verbose_name_plural = 'Соц. сети'
        ordering = ['sort']
