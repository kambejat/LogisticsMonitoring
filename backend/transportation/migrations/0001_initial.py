# Generated by Django 5.0.6 on 2024-06-03 16:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportationEfficiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.IntegerField()),
                ('fuel_consumption', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vehicle_utilization', models.DecimalField(decimal_places=2, max_digits=5)),
                ('average_delivery_time', models.IntegerField()),
                ('route_efficiency', models.DecimalField(decimal_places=2, max_digits=5)),
                ('notes', models.TextField(blank=True, null=True)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_transportations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TransportationEfficiency',
            },
        ),
    ]
