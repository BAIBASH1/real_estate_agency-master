# Generated by Django 2.2.24 on 2023-05-03 14:18

import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20230430_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца:'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца:')),
                ('flats', models.ManyToManyField(blank=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности: ')),
            ],
        ),
    ]
