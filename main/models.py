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
