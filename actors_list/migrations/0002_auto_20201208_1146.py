# Generated by Django 3.1.3 on 2020-12-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serial',
            name='release_year',
            field=models.DateField(blank=True),
        ),
    ]