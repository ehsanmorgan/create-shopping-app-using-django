# Generated by Django 4.1.7 on 2023-03-10 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import order.ultis.genirite_code


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0012_reviews_jewellery'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odrder_code', models.CharField(default=order.ultis.genirite_code.genirite_code, max_length=12)),
                ('order_status', models.CharField(choices=[('Recevied', 'Recevied'), ('Processed', 'Processed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Recevied', max_length=12)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='order_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField(default=1)),
                ('total', models.FloatField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='odere_detail', to='order.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_product', to='shop.electronic')),
            ],
        ),
    ]