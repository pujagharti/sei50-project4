# Generated by Django 3.1.2 on 2020-10-27 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emojis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emoji',
            name='image',
            field=models.CharField(max_length=99999),
        ),
    ]
