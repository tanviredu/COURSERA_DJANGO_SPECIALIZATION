# Generated by Django 3.1.1 on 2020-09-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='area_hectares',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='site',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='site',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
