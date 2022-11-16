from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=100, verbose_name='Маршрут', unique=True)
    travel_times = models.PositiveIntegerField(verbose_name='Время')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Откуда',
                                  related_name='route_from_city_set')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Куда', related_name='route_to_city_set')
    trains = models.ManyToManyField('trains.Train', verbose_name='Список поездов')

    def __str__(self):
        return f'Маршрут №{self.name} из города {self.from_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['travel_times']

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Изменить город прибытия')
        qs = Route.objects.filter(from_city=self.from_city, to_city=self.to_city,
                                  travel_times=self.travel_times).exclude(pk=self.pk)
        if qs.exists():
            return ValidationError('Изменить время в пути')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
