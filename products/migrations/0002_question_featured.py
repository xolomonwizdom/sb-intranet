# Generated by Django 3.0.6 on 2020-06-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
