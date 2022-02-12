# Generated by Django 3.1.3 on 2020-11-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_category', models.CharField(max_length=200)),
                ('product_desc', models.CharField(max_length=200)),
                ('product_model', models.CharField(max_length=200)),
                ('product_price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]