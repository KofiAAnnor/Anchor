# Generated by Django 3.0.7 on 2020-06-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200622_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='This is a description of the current item.Descriptions are meant to tell the user more about our products', max_length=100),
        ),
    ]
