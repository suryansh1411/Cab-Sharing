# Generated by Django 3.0.3 on 2020-05-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200428_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='hostel',
            field=models.CharField(choices=[('Brahmaputra', 'Brahmaputra'), ('Dihing', 'Dihing'), ('Manas', 'Manas'), ('Lohit', 'Lohit'), ('Dhansiri', 'Dhansiri'), ('Kapili', 'Kapili'), ('Siang', 'Siang'), ('Kameng', 'Kameng'), ('Umiam', 'Umiam'), ('Barak', 'Barak'), ('Subhansiri', 'Subhansiri'), ('Disang/Dibang', 'Disang/Dibang')], max_length=50),
        ),
    ]