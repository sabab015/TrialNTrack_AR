# Generated by Django 3.1.3 on 2020-12-28 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0014_auto_20201228_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(),
        ),
    ]
