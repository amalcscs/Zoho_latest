# Generated by Django 3.2.20 on 2023-12-05 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0064_deletedestimates'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalentry',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchase_order',
            name='adjustment_charge',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchase_order',
            name='convert_status',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AddField(
            model_name='purchase_order',
            name='payed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchase_order',
            name='payment_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
