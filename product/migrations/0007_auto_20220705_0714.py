# Generated by Django 3.2.13 on 2022-07-05 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertyname',
            options={'verbose_name': 'Property Name', 'verbose_name_plural': 'Property Names'},
        ),
        migrations.AlterField(
            model_name='propertyname',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='propertynames', to='product.category'),
        ),
    ]