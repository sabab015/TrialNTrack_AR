# Generated by Django 3.1.3 on 2020-12-28 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0013_auto_20201228_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.CharField(max_length=200),
        ),
    ]