# Generated by Django 4.0.4 on 2022-04-17 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('salary', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('dateofbirth', models.CharField(max_length=20, null=True)),
                ('phonenumber', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_Branches',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phonenumber', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True)),
                ('dateofbirth', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]