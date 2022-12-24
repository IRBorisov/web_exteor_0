from django.db import models

class Articles(models.Model):
    schema = models.CharField('Название', max_length=100)
    name = models.CharField('Имя', max_length=100)
    type = models.CharField('Тип', max_length=100)
    rs_definition = models.CharField('РС-определение', max_length=300)
    term = models.CharField('Термин', max_length=500)
    text_definition = models.TextField('Текстовое определение')


    def __str__(self):
        return self.schema

    def get_absolute_url(self):
        return '/news/{}'.format(self.id)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'