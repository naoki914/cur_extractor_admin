# Generated by Django 4.0.1 on 2022-02-21 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_storageinfo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportinfo',
            name='prefix',
        ),
    ]
