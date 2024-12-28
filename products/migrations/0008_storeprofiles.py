# Generated by Django 4.2.16 on 2024-11-25 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_delevary_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='storeprofiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_name', models.CharField(max_length=100)),
                ('sp_location', models.CharField(max_length=100)),
                ('sp_number', models.CharField(max_length=100)),
                ('sp_salary', models.IntegerField(default=0)),
                ('sp_others', models.CharField(max_length=100)),
                ('sp_photo', models.ImageField(default='default.jpg', upload_to='')),
                ('password', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
