# Generated by Django 5.0.7 on 2024-08-01 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='reorder_level',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]