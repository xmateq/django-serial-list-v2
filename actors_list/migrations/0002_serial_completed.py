# Generated by Django 3.1.3 on 2020-11-24 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serial',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
