# Generated by Django 3.2.3 on 2021-05-31 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coviddata',
            name='clasificacion_final',
            field=models.CharField(max_length=150),
        ),
    ]
