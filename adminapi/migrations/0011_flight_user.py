# Generated by Django 4.2.5 on 2024-02-25 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0010_alter_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapi.user'),
        ),
    ]
