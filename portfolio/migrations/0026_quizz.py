# Generated by Django 4.0.4 on 2022-05-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0025_alter_lingua_nivel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta1', models.IntegerField(max_length=4)),
                ('pergunta2', models.CharField(max_length=20)),
                ('pergunta3', models.CharField(max_length=20)),
                ('pergunta4', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
    ]