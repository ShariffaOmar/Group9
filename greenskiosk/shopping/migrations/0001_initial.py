# Generated by Django 3.1 on 2020-09-06 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('shipping', '0001_initial'),
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(max_length=100)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('date_placed', models.DateTimeField()),
                ('status', models.CharField(max_length=60)),
                ('delivery_time', models.DateTimeField()),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.cart')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_of_payment', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shopping.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shopping.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.shippingprovider'),
        ),
    ]
