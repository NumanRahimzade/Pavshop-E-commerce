# Generated by Django 3.1 on 2022-03-31 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_billingdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BillingDetails',
            new_name='BillingDetail',
        ),
    ]
