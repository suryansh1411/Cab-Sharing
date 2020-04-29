from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
# Create your models here.

GENDER=[
    ('both','all'),
    ('girls','only girls'),
    ('boys', 'only boys')
]


class Booking(models.Model):
    creator=models.CharField(max_length=30, blank=False)
    time=models.TimeField( blank=False, auto_now=False, auto_now_add=False ,default='00:00 AM')
    date=models.DateField(blank=False, auto_now=False, auto_now_add=False ,default='2019-6-14')
    start_position=models.CharField(max_length=30, blank=False)
    destination=models.CharField(max_length=30, blank=False)
    max_members=models.PositiveIntegerField(default=4, blank=False, help_text='maximum number of members includes you as well.')
    gender=models.CharField(default='both', max_length=20, choices=GENDER)
    

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




class Chat(models.Model):
    booking=models.ForeignKey('Booking', on_delete=models.CASCADE , related_name='chats', null=True)
    name=models.CharField(max_length=90, null=True)
    message=models.CharField(max_length=500, null=True)
    photo=models.ImageField( null=True)
    time=models.TimeField(default=timezone.localtime)

    def get_absolute_url(self):
        return redirect('booking:chats_display', kwargs={'pk':self.booking.pk})
