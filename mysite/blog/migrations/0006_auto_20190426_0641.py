# Generated by Django 2.2 on 2019-04-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190426_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='hello-world', unique=True),
            preserve_default=False,
        ),
    ]
