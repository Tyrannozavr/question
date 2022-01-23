# Generated by Django 4.0.1 on 2022-01-22 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_alter_exam_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.IntegerField(null=True)),
                ('label', models.BooleanField(verbose_name='Нужно выучить')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={},
        ),
        migrations.RemoveField(
            model_name='exam',
            name='label',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='question',
        ),
        migrations.AddField(
            model_name='exam',
            name='quantity_questions',
            field=models.IntegerField(null=True, verbose_name='Количество вопросов'),
        ),
        migrations.AddField(
            model_name='exam',
            name='time_exam',
            field=models.DateTimeField(null=True, verbose_name='Дата экзамена'),
        ),
    ]
