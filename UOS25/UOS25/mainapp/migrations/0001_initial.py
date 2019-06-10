# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-10 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('mileage', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('gender', models.DecimalField(decimal_places=0, max_digits=4, null=True)),
                ('birthday', models.DateField(null=True)),
                ('contact', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_refund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refund_timestamp', models.DateTimeField()),
                ('refund_reason_code', models.DecimalField(decimal_places=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('daytime_hourpay', models.DecimalField(decimal_places=0, default=6800, max_digits=10, null=True)),
                ('nighttime_hourpay', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('employed_date', models.DateField()),
                ('fire_date', models.DateField(null=True)),
                ('contact', models.CharField(max_length=20)),
                ('position_code', models.DecimalField(decimal_places=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Franchise_store_rcpt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rcpt_date', models.DateField()),
                ('rcpt_amount', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance_cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_cost_code', models.DecimalField(decimal_places=0, max_digits=4)),
                ('amount', models.DecimalField(decimal_places=0, max_digits=10)),
                ('process_date', models.DateField()),
                ('etc', models.CharField(max_length=80, null=True)),
                ('storeowner_check', models.CharField(default='N', max_length=1)),
                ('employee_id', models.ForeignKey(db_column='employee_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_timestamp', models.DateTimeField()),
                ('complete_timestamp', models.DateTimeField(null=True)),
                ('process_code', models.DecimalField(decimal_places=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Order_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=6)),
                ('sent_timestamp', models.DateTimeField(null=True)),
                ('arrival_timestamp', models.DateTimeField(null=True)),
                ('process_code', models.DecimalField(decimal_places=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('barcode', models.DecimalField(decimal_places=0, max_digits=13, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('supply_price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('category_a', models.DecimalField(decimal_places=0, max_digits=4)),
                ('category_b', models.DecimalField(decimal_places=0, max_digits=4)),
                ('explain', models.CharField(max_length=80, null=True)),
                ('picture_file_path', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_timestamp', models.DateTimeField()),
                ('payment_method_code', models.DecimalField(decimal_places=0, max_digits=4)),
                ('payment_information', models.CharField(max_length=30, null=True)),
                ('customer_id', models.ForeignKey(db_column='customer_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Customer')),
                ('employee_id', models.ForeignKey(db_column='employee_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_location_code', models.DecimalField(decimal_places=0, max_digits=4)),
                ('quantity', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('barcode', models.ForeignKey(db_column='barcode', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=80)),
                ('contact', models.CharField(max_length=20)),
                ('store_pay', models.FloatField()),
                ('store_code', models.DecimalField(decimal_places=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Store_refund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=6)),
                ('refund_timestamp', models.DateTimeField()),
                ('refund_reason_code', models.DecimalField(decimal_places=0, max_digits=4)),
                ('process_code', models.DecimalField(decimal_places=0, max_digits=4)),
                ('barcode', models.ForeignKey(db_column='barcode', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product')),
                ('store_id', models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('contact', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Trade_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=6)),
                ('is_refund', models.CharField(default='N', max_length=1)),
                ('barcode', models.ForeignKey(db_column='barcode', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product')),
                ('receipt_id', models.ForeignKey(db_column='receipt_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Receipt')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('employee_id', models.ForeignKey(db_column='employee_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Employee')),
                ('store_id', models.ForeignKey(db_column='store_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Work_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workstart_timestamp', models.DateTimeField()),
                ('workend_timestamp', models.DateTimeField()),
                ('storeowner_check', models.CharField(default='N', max_length=1)),
                ('employee_id', models.ForeignKey(db_column='employee_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='store_id',
            field=models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Store'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='store_id',
            field=models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Store'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier_id',
            field=models.ForeignKey(db_column='supplier_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Supplier'),
        ),
        migrations.AddField(
            model_name='order_list',
            name='barcode',
            field=models.ForeignKey(db_column='barcode', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product'),
        ),
        migrations.AddField(
            model_name='order_list',
            name='order_id',
            field=models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='store_id',
            field=models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Store'),
        ),
        migrations.AddField(
            model_name='maintenance_cost',
            name='store_id',
            field=models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Store'),
        ),
        migrations.AddField(
            model_name='franchise_store_rcpt',
            name='store_id',
            field=models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Store'),
        ),
        migrations.AddField(
            model_name='employee',
            name='store_id',
            field=models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Store'),
        ),
        migrations.AddField(
            model_name='customer_refund',
            name='trade_list_id',
            field=models.ForeignKey(db_column='trade_list_id', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Trade_list'),
        ),
    ]
