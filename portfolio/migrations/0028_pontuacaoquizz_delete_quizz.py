# Generated by Django 4.0.4 on 2022-05-25 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0027_alter_quizz_pergunta1'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontuacaoQuizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('apelido', models.CharField(max_length=30)),
                ('pontuacao', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Quizz',
        ),
    ]
