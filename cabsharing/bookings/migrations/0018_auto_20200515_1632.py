# Generated by Django 3.0.3 on 2020-05-15 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0017_auto_20200511_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='approved',
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=500)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbackers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
