# Generated by Django 3.1 on 2022-05-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20220509_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_az',
            field=models.CharField(max_length=70, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=70, null=True, verbose_name='Name'),
        ),
    ]
