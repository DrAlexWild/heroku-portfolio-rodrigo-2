# Generated by Django 4.0.4 on 2022-05-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_cadeira_ano_letivo_alter_pessoa_link_linkedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='nome',
            field=models.CharField(max_length=30),
        ),
    ]