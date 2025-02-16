# Generated by Django 5.1.6 on 2025-02-11 22:32

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=50, unique=True)),
                ('product_description_short', models.CharField(max_length=255)),
                ('product_description_long', models.TextField(blank=True, null=True)),
                ('product_unit_price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('product_stock', models.IntegerField(default=0)),
                ('product_thumbnail_url', models.CharField(blank=True, max_length=500, null=True)),
                ('product_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('product_sku', models.CharField(max_length=100, unique=True)),
                ('product_dimensions', models.CharField(blank=True, max_length=255, null=True)),
                ('product_weight', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('product_height', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('product_width', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('product_length', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('product_image_url', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('product_created_at', models.DateTimeField(auto_now_add=True)),
                ('product_updated_at', models.DateTimeField(auto_now=True)),
                ('product_is_active', models.BooleanField(default=True)),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
