# Generated by Django 4.0.4 on 2022-05-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_alter_publicacao_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='link_lusofona',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='tecnologias',
        ),
        migrations.AddField(
            model_name='projeto',
            name='tecnologias',
            field=models.ManyToManyField(to='portfolio.tecnologia'),
        ),
    ]
