# Generated by Django 5.0 on 2023-12-27 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('school', '0006_schooldbmodel_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_profile', to='account.useraccountmodel'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='school',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_profile', to='school.schoolinfomodel'),
        ),
    ]
