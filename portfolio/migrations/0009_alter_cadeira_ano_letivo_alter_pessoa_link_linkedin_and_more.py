# Generated by Django 4.0.4 on 2022-05-17 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_professor_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='ano_letivo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='link_linkedin',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='link_linkedin',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='linkGitHub',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='linkYt',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
