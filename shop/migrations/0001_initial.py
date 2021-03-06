# Generated by Django 4.0.2 on 2022-03-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('amount', models.IntegerField()),
                ('size', models.CharField(max_length=6)),
                ('company_name', models.CharField(max_length=300)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('weight', models.CharField(max_length=10)),
            ],
        ),
    ]
