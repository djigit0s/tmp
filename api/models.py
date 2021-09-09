from django.db import models

MEASURE_CHOICES = [
    ('Штук', 'Штук'),
    ('Килoгрaмм', 'Килoгрaмм'),
    ('Литр', 'Литр'),
]


class Product(models.Model):
    """
    Товары на складе
    """
    title = models.CharField('Наименование', max_length=300)
    stock = models.PositiveIntegerField('Количество')
    measure = models.CharField(
        'Едицина измерения', max_length=50, choices=MEASURE_CHOICES)
    price = models.PositiveIntegerField('Цена')
    updated_at = models.DateTimeField(
        'Дата и время последнего изменения', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
