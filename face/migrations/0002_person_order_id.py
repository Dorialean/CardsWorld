# Generated by Django 4.0.2 on 2022-03-06 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='order_id',
            field=models.ForeignKey(default='No order', on_delete=django.db.models.deletion.CASCADE, to='shop.order'),
        ),
    ]
