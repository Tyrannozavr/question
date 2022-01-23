from django.db import models


class Questions(models.Model):
    question = models.IntegerField(null=True)
    label = models.BooleanField(verbose_name='Нужно выучить')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return str(self.question)

class Exam(models.Model):
    time_exam = models.DateTimeField(verbose_name='Дата экзамена', null=True)
    quantity_questions = models.IntegerField(verbose_name='Количество вопросов', null=True)

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамен'

    def __str__(self):
        return str(self.quantity_questions)