# Generated by Django 4.2.1 on 2023-06-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0004_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
