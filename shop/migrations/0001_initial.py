# Generated by Django 4.1.7 on 2023-03-04 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fashion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='shoping/')),
                ('price', models.FloatField()),
                ('flag', models.CharField(choices=[('English', 'English'), ('France', 'France')], max_length=30)),
                ('quantity', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
