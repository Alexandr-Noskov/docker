from django.db import models
from django.conf import settings



class Document(models.Model):
    STATUS_ACCEPTED = 'ok'
    STATUS_DENIED = 'denied'
    STATUSES = (
        (STATUS_ACCEPTED, 'Принят'),
        (STATUS_DENIED, 'Отклонен'),
    )

    status = models.CharField(max_length=20, choices=STATUSES,)

    # Строковое представления для разработчиков
    def __str__(self):
        return f'Документ {self.owner} Принятие - {self.check_file} Отклонение - {self.checkout_file}'

    # Мета представление, например для админки
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
