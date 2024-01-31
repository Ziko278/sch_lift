# Generated by Django 5.0 on 2023-12-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_schoolinfomodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolinfomodel',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE')], default='active', max_length=30),
        ),
    ]