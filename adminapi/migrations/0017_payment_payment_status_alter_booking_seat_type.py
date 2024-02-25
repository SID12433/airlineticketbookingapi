# Generated by Django 4.2.5 on 2024-02-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0016_alter_booking_amount_alter_booking_seat_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Completed', max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='seat_type',
            field=models.CharField(choices=[('Economy', 'Economy'), ('Premium Economy', 'Premium Economy'), ('Business', 'Business')], default='Economy', max_length=50),
        ),
    ]
