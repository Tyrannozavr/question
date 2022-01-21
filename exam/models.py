from django.db import models


class Exam(models.Model):
    question = models.IntegerField()
    label = models.BooleanField(verbose_name='Нужно выучить')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return str(self.question)
