# Generated by Django 2.0 on 2018-06-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20180628_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]
