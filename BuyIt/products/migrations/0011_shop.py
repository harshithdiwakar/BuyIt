# Generated by Django 2.1.2 on 2019-10-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20191008_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop',
            fields=[
                ('category', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('slug', models.SlugField()),
            ],
        ),
    ]