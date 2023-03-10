# Generated by Django 4.1.7 on 2023-03-08 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0008_remove_reviews_jewellery_100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment1', models.TextField(max_length=200)),
                ('createt_at1', models.DateTimeField(default=django.utils.timezone.now)),
                ('fashion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fashion_review', to='shop.fashion')),
                ('user1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_author1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
