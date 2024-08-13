# Generated by Django 4.2.1 on 2023-07-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='coupon_code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='discount_amount',
            field=models.FloatField(default=0.0),
        ),
    ]
