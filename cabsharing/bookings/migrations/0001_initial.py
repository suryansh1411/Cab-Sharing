# Generated by Django 3.0.3 on 2020-04-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=30)),
                ('cab_timing', models.DateTimeField()),
                ('start_position', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
            ],
        ),
    ]