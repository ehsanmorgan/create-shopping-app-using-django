# Generated by Django 4.1.7 on 2023-03-10 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0011_remove_reviews1_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews_Jewellery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment2', models.TextField(max_length=200)),
                ('createt_at2', models.DateTimeField(default=django.utils.timezone.now)),
                ('jewellery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jewellery_review', to='shop.jewellery')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_author2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
