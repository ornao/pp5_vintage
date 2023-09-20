# Generated by Django 3.2.21 on 2023-09-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('never worn', 'Never worn'), ('very good', 'Very Good'), ('good', 'Good'), ('fair', 'Fair')], max_length=100),
        ),
    ]