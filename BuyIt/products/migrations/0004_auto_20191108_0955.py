# Generated by Django 2.2.5 on 2019-11-08 09:55

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_shop_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='display',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_shop_image_path),
        ),
        migrations.AddField(
            model_name='shop',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_shop_image_path),
        ),
        migrations.AddField(
            model_name='shop',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_shop_image_path),
        ),
        migrations.AddField(
            model_name='shop',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_shop_image_path),
        ),
        migrations.AddField(
            model_name='shop',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_shop_image_path),
        ),
    ]
