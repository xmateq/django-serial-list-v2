# Generated by Django 3.1.3 on 2020-11-28 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors_list', '0009_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='raiting',
            new_name='rate',
        ),
    ]
