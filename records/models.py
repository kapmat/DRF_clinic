from django.db import models


class Records(models.Model):
    service = models.ForeignKey(
        'root.Services',
        on_delete=models.CASCADE,
        verbose_name='Услуга',
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
    )
    record_time = models.DateTimeField(
        verbose_name='Время записи',
    )
    visitors_name = models.CharField(
        max_length=50,
        verbose_name='Имя клиента',
    )
    visitors_email = models.EmailField(
        max_length=50,
        verbose_name='Email клиента',
    )
    visitors_phone = models.CharField(
        max_length=18,
        verbose_name='Номер телефона клиента',
    )

    def __str__(self):
        return "{}, {}".format(self.visitors_name, self.service, self.record_time)
