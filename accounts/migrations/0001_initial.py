# Generated by Django 4.0.1 on 2022-01-24 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='ReportInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('prefix', models.CharField(max_length=128)),
                ('in_use', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'report_info',
            },
        ),
        migrations.CreateModel(
            name='StorageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket_name', models.CharField(max_length=63)),
                ('account_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('report_info_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.reportinfo')),
            ],
            options={
                'db_table': 'storage_info',
            },
        ),
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_key', models.CharField(max_length=128)),
                ('secret_key', models.CharField(max_length=1024)),
                ('account_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('report_info_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.reportinfo')),
            ],
            options={
                'db_table': 'credential',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.company'),
        ),
    ]
