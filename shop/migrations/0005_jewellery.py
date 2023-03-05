# Generated by Django 4.1.7 on 2023-03-05 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_electronic_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jewellery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='jewellery/')),
                ('price', models.FloatField()),
                ('flag', models.CharField(choices=[('English', 'English'), ('France', 'France')], max_length=30)),
                ('quantity', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
