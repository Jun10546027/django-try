# Generated by Django 2.2 on 2019-04-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190426_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
