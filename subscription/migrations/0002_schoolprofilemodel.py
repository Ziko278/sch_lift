# Generated by Django 5.0 on 2023-12-23 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_schoolformmodel_schoolinfomodel_short_name_and_more'),
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.FloatField(default=0)),
                ('current_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subscription.planmodel')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.schoolinfomodel')),
            ],
        ),
    ]