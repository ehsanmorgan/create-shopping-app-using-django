# Generated by Django 4.1.7 on 2023-03-08 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_reviews_jewellery_100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='jewellery_100',
        ),
    ]
