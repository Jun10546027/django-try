# Generated by Django 2.2 on 2019-05-05 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190505_1336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', 'update', 'timestamp']},
        ),
    ]