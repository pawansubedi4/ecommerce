# Generated by Django 4.2.16 on 2024-11-25 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_delete_orders_delete_products_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delevary',
            name='password',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
