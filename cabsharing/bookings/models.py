from django.db import models
from django.shortcuts import redirect
# Create your models here.



class Bookings(models.Model):
    creator=models.CharField(max_length=30, blank=False)
    # cab_timing=models.DateTimeField( blank=False)
    cab_timing=models.CharField(max_length=90, blank=False)

    start_position=models.CharField(max_length=30, blank=False)
    destination=models.CharField(max_length=30, blank=False)
    max_members=models.PositiveIntegerField(default=4, blank=False, help_text='maximum number of members includes you as well.')


    def get_absolute_url(self):
        return redirect('index')


    def set_admin(self):
        self.creator={{user.username}}
