# Generated by Django 2.0.7 on 2018-08-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_auto_20180815_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
