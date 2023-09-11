# Generated by Django 4.2.5 on 2023-09-08 15:23

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('sold_to', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('or_number', models.CharField(max_length=200)),
                ('total_amount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=50)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('remarks', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]