# Generated by Django 2.2.24 on 2023-09-16 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20230916_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint',
            new_name='text',
        ),
    ]
