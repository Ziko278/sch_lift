# Generated by Django 5.0 on 2023-12-28 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0004_delete_schoolprofilemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionpaymentmodel',
            name='all_time_balance',
        ),
        migrations.RemoveField(
            model_name='subscriptionpaymentmodel',
            name='current_balance',
        ),
        migrations.RemoveField(
            model_name='subscriptionpaymentmodel',
            name='previous_balance',
        ),
    ]