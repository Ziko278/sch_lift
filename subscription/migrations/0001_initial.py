# Generated by Django 5.0 on 2023-12-16 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_dashboard', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModuleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('years_of_backup', models.IntegerField(default=5)),
                ('price_per_term', models.FloatField()),
                ('features', models.ManyToManyField(blank=True, to='subscription.featuremodel')),
                ('modules', models.ManyToManyField(blank=True, to='subscription.modulemodel')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subscription.planmodel')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.schoolinfomodel')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionPaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('1st term', '1st TERM'), ('2nd term', '2nd TERM'), ('3rd term', '3rd TERM')], max_length=10)),
                ('previous_balance', models.FloatField()),
                ('amount', models.FloatField()),
                ('current_balance', models.FloatField()),
                ('all_time_balance', models.FloatField()),
                ('payment_method', models.CharField(choices=[('1st term', '1st TERM'), ('2nd term', '2nd TERM'), ('3rd term', '3rd TERM')], max_length=10)),
                ('proof_of_payment', models.FileField(blank=True, null=True, upload_to='subscription/payment')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.schoolinfomodel')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.sessionmodel')),
            ],
        ),
    ]
