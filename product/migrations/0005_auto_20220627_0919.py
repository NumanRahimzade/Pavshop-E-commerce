# Generated by Django 3.2.13 on 2022-06-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_review_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='productversion',
            name='new_price',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='NewPrice'),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], default=1, verbose_name='Rating'),
        ),
    ]