# Generated by Django 4.0.4 on 2022-05-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_interesse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesse',
            name='descricao',
            field=models.TextField(max_length=1000),
        ),
    ]
