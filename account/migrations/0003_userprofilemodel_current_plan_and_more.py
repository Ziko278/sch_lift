# Generated by Django 5.0 on 2023-12-27 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_userprofilemodel_account_and_more'),
        ('subscription', '0004_delete_schoolprofilemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='current_plan',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subscription.planmodel'),
        ),
        migrations.AddField(
            model_name='userprofilemodel',
            name='wallet',
            field=models.FloatField(default=0),
        ),
    ]
