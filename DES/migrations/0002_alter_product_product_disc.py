# Generated by Django 3.2.5 on 2022-01-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DES', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_disc',
            field=models.IntegerField(),
        ),
    ]
