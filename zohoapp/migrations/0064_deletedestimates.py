# Generated by Django 3.2.20 on 2023-12-05 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0063_auto_20231205_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='deletedestimates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=50)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.company_details')),
            ],
        ),
    ]
