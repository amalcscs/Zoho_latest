# Generated by Django 3.2.20 on 2023-11-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0043_auto_20231028_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasebills',
            name='bill_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasebills',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
