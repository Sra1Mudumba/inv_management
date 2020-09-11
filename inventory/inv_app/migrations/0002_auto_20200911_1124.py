# Generated by Django 3.1 on 2020-09-11 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cust_Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField(max_length=10)),
                ('total_price', models.FloatField(max_length=10)),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv_app.invoice')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerSale',
        ),
    ]
