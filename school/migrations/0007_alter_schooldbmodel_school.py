# Generated by Django 5.0 on 2023-12-27 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_schooldbmodel_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooldbmodel',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_db', to='school.schoolinfomodel'),
        ),
    ]
