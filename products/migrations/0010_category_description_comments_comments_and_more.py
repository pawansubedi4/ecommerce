# Generated by Django 4.2.16 on 2024-11-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='non'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comments',
            field=models.TextField(blank=True, default='non', null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='phone_number',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
