# Generated by Django 3.1 on 2022-05-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='title_az',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_en',
            field=models.CharField(max_length=30, null=True),
        ),
    ]