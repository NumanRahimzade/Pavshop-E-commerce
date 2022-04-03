# Generated by Django 3.1 on 2022-04-01 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Sub-Total')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('firstname', models.CharField(max_length=70, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=70, verbose_name='Last Name')),
                ('companyname', models.CharField(max_length=80, verbose_name='Company Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('town', models.CharField(max_length=70, verbose_name='Town/City')),
                ('country', models.CharField(max_length=70, verbose_name='Country')),
                ('email', models.EmailField(max_length=50, verbose_name='Email Address')),
                ('phone', models.CharField(max_length=40, verbose_name='Phone')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
                ('basket', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='order.basket')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Sub-Total')),
                ('count', models.IntegerField(verbose_name='Count')),
                ('basket', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='order.basket')),
                ('productVersion', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.productversion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
