from django.contrib.auth.models import User
from django.db import models


class Records(models.Model):
    service = models.ForeignKey(
        'services.services',
        on_delete=models.CASCADE,
        verbose_name='Услуга',
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
    )
    record_time = models.DateTimeField(
        verbose_name='Время записи',
    )
    visitors_email = models.EmailField(
        max_length=50,
        verbose_name='Email клиента',
    )
    visitors_phone = models.CharField(
        max_length=18,
        verbose_name='Номер телефона клиента',
    )
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{}, {}, {}".format(self.user, self.service, self.record_time)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

