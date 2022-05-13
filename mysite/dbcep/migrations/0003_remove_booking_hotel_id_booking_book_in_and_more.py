# Generated by Django 4.0.4 on 2022-04-18 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbcep', '0002_rooms_employees_hotel_id_hotel_branches_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Hotel_id',
        ),
        migrations.AddField(
            model_name='booking',
            name='Book_in',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='Book_out',
            field=models.CharField(default=23, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='Customer_id',
            field=models.ForeignKey(default=34, on_delete=django.db.models.deletion.CASCADE, to='dbcep.customers'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='Bookingtype',
            field=models.CharField(max_length=100),
        ),
    ]