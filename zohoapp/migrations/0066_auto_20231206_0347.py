# Generated by Django 3.2.20 on 2023-12-06 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0065_auto_20231205_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankHolders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder_name', models.CharField(blank=True, max_length=200, null=True)),
                ('alias_name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.BigIntegerField(blank=True, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('acc_type', models.CharField(blank=True, default='Bank', max_length=200, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=200, null=True)),
                ('acc_number', models.BigIntegerField(blank=True, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=200, null=True)),
                ('swift_code', models.CharField(blank=True, max_length=200, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=200, null=True)),
                ('cheque_range', models.CharField(blank=True, max_length=200, null=True)),
                ('cheque_printing', models.CharField(blank=True, max_length=200, null=True)),
                ('cheque_print_config', models.CharField(blank=True, max_length=200, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=200, null=True)),
                ('registration_type', models.CharField(blank=True, max_length=200, null=True)),
                ('gstin', models.CharField(blank=True, max_length=200, null=True)),
                ('gst_alter', models.CharField(blank=True, max_length=200, null=True)),
                ('mail_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mail_address', models.TextField(blank=True, null=True)),
                ('mail_country', models.CharField(blank=True, max_length=200, null=True)),
                ('mail_state', models.CharField(blank=True, max_length=200, null=True)),
                ('mail_pin', models.CharField(blank=True, max_length=200, null=True)),
                ('openbal_date', models.DateField(blank=True, null=True)),
                ('openbal_type', models.CharField(blank=True, max_length=200, null=True)),
                ('openbal_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('status', models.CharField(blank=True, default='Active', max_length=15, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.bankcreation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoanAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_name', models.CharField(blank=True, max_length=200, null=True)),
                ('acc_number', models.BigIntegerField(blank=True, null=True)),
                ('lender_bank', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('loan_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('loan_date', models.DateField(blank=True, null=True)),
                ('amount_received', models.CharField(blank=True, max_length=200, null=True)),
                ('amt_rcvd_cheque_id', models.CharField(blank=True, max_length=200, null=True)),
                ('amt_rcvd_upi_id', models.CharField(blank=True, max_length=200, null=True)),
                ('amt_rcvd_bank_acc_number', models.BigIntegerField(blank=True, null=True)),
                ('interest', models.FloatField(blank=True, default=0.0, null=True)),
                ('term_duration', models.IntegerField(blank=True, default=0, null=True)),
                ('procs_fee', models.FloatField(blank=True, default=0.0, null=True)),
                ('procs_fee_paid_from', models.CharField(blank=True, max_length=200, null=True)),
                ('procs_fee_cheque_id', models.CharField(blank=True, max_length=200, null=True)),
                ('procs_fee_upi_id', models.CharField(blank=True, max_length=200, null=True)),
                ('procs_fee_bank_acc_number', models.BigIntegerField(blank=True, null=True)),
                ('status', models.CharField(default='Active', max_length=200, null=True)),
                ('holder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.bankholders')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='setting_list',
            name='bank_holders',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='setting_list',
            name='loan_account',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.CreateModel(
            name='LoanAccountTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('principal', models.FloatField(blank=True, default=0.0, null=True)),
                ('interest', models.FloatField(blank=True, default=0.0, null=True)),
                ('total', models.FloatField(blank=True, default=0.0, null=True)),
                ('balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('emi_paid', models.CharField(blank=True, max_length=200, null=True)),
                ('emi_paid_cheque_id', models.CharField(blank=True, max_length=200, null=True)),
                ('emi_paid_upi_id', models.CharField(blank=True, max_length=200, null=True)),
                ('emi_paid_bank_acc_number', models.BigIntegerField(blank=True, null=True)),
                ('additional_loan_received_from', models.CharField(blank=True, max_length=200, null=True)),
                ('add_loan_cheque_id', models.CharField(blank=True, max_length=200, null=True)),
                ('add_loan_upi_id', models.CharField(blank=True, max_length=200, null=True)),
                ('add_loan_bank_acc_number', models.BigIntegerField(blank=True, null=True)),
                ('loan_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.loanaccounts')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
