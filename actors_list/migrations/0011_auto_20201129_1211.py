# Generated by Django 3.1.3 on 2020-11-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors_list', '0010_auto_20201128_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]
