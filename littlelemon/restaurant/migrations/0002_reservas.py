# Generated by Django 5.2.3 on 2025-06-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.IntegerField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('No_of_guest', models.IntegerField(max_length=6)),
                ('bookingdate', models.DateTimeField()),
            ],
        ),
    ]
