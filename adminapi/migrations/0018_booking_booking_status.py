# Generated by Django 4.2.5 on 2024-02-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0017_payment_payment_status_alter_booking_seat_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]
