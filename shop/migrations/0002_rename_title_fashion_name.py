# Generated by Django 4.1.7 on 2023-03-04 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fashion',
            old_name='title',
            new_name='name',
        ),
    ]
