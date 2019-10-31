# Generated by Django 2.2.5 on 2019-10-31 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20191031_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='all', on_delete=django.db.models.deletion.CASCADE, to='products.Product_Category'),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Shop'),
        ),
    ]
