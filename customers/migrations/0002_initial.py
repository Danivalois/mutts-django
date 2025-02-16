# Generated by Django 5.1.6 on 2025-02-11 22:32

import customers.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_cpf', models.CharField(max_length=11, unique=True, validators=[customers.models.validate_cpf])),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('customer_created_at', models.DateTimeField(auto_now_add=True)),
                ('customer_is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=8)),
                ('street', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('house_number', models.CharField(max_length=20)),
                ('complement', models.CharField(blank=True, max_length=255, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='customers.customer')),
            ],
        ),
    ]
