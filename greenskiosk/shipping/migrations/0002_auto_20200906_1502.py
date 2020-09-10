# Generated by Django 3.1 on 2020-09-06 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipping', '0001_initial'),
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.order'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='shipping_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.shippingprovider'),
        ),
    ]
