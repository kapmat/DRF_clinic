from django.db import models


class Services(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название услуги'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Описание услуги',
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Стоимость услуги'
    )
    service_status = models.BooleanField(
        default=True,
        verbose_name='Услуга доступна',
    )

    def __str__(self):
        return str(self.title)
