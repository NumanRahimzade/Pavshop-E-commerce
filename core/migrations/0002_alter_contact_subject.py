# Generated by Django 4.0.2 on 2022-03-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=50, verbose_name='Movzu'),
        ),
    ]
