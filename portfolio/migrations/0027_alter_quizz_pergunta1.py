# Generated by Django 4.0.4 on 2022-05-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0026_quizz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='pergunta1',
            field=models.IntegerField(),
        ),
    ]
