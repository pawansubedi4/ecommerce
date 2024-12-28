# Generated by Django 4.2.16 on 2024-11-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products1223432123'),
    ]

    operations = [
        migrations.AddField(
            model_name='delevary',
            name='dm_salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ordersnew',
            name='o_discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ordersnew',
            name='o_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ordersnew',
            name='o_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='p_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products1223432123',
            name='p_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productsnew',
            name='p_discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productsnew',
            name='p_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productsnew',
            name='p_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='products1223432123',
            name='p_name',
            field=models.CharField(max_length=100),
        ),
    ]
