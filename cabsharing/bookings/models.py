from django.db import models
from django.shortcuts import redirect
# Create your models here.



class Booking(models.Model):
    creator=models.CharField(max_length=30, blank=False)
    time=models.TimeField( blank=False, auto_now=False, auto_now_add=False ,default='00:00 AM')
    date=models.DateField(blank=False, auto_now=False, auto_now_add=False ,default='2019-6-14')
    start_position=models.CharField(max_length=30, blank=False)
    destination=models.CharField(max_length=30, blank=False)
    max_members=models.PositiveIntegerField(default=4, blank=False, help_text='maximum number of members includes you as well.')


    def get_absolute_url(self):
        return redirect('index')


    def approved_members(self):
        return self.bookings.filter(approved=True)

    #
    # def set_admin(self):
    #     self.creator={{user.username}}



class Member(models.Model):
    booking=models.ForeignKey('Booking', on_delete=models.CASCADE , related_name='members')
    name=models.CharField(max_length=90)
    approved=models.BooleanField(default=False)


    def member_approval(self):
        self.approved=True
        self.save()

    def get_absolute_url(self):
        return reverse('index')
