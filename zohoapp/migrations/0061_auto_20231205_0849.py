# Generated by Django 3.2.20 on 2023-12-05 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0060_ewaybillidmodel_ewaycomments_paymentrecievedallinvoices_paymentrecievedcomments_paymentrecievedidmod'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimates',
            name='balance',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='estimates',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.company_details'),
        ),
        migrations.AddField(
            model_name='estimates',
            name='convert_recinvoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='estimates',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.invoice'),
        ),
        migrations.AddField(
            model_name='estimates',
            name='reccinvoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.recurring_invoice'),
        ),
        migrations.AddField(
            model_name='estimates',
            name='salesorder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.salesorder'),
        ),
        migrations.AddField(
            model_name='expensee',
            name='accno',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachment/'),
        ),
        migrations.AddField(
            model_name='expensee',
            name='bankid',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='cgst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='chequeno',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='customer_place_supply',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='customername',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='igst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='reference_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='sgst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='status',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='upiid',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='vendor_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='expensee',
            name='vendor_place_supply',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='estimates',
            name='reference',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expensee',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='expense_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('expense', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.expensee')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='deletedexpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=50)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.company_details')),
            ],
        ),
    ]
