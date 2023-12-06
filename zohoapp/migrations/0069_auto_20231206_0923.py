# Generated by Django 3.2.20 on 2023-12-06 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0068_recurring_invoice_estimate'),
    ]

    operations = [
        migrations.AddField(
            model_name='retaineritems',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.additem'),
        ),
        migrations.AddField(
            model_name='sales_item',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.additem'),
        ),
    ]
