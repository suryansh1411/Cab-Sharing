
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

GENDER=[
    ('all','all'),
    ('girls only','girls only'),
    ('boys only', 'boys only')
]

 
class Booking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', null=True)
    creator=models.CharField(max_length=30, blank=False)
    time=models.TimeField( blank=False, auto_now=False, auto_now_add=False ,default='00:00 AM')
    date=models.DateField(blank=False, auto_now=False, auto_now_add=False ,default='2019-6-14')
    start_position=models.CharField(max_length=30, blank=False)
    destination=models.CharField(max_length=30, blank=False)
    max_members=models.PositiveIntegerField(default=4, blank=False, help_text='maximum number of members includes you as well.')
    gender=models.CharField(default='both', max_length=20, choices=GENDER)
    description=models.CharField(blank=True, null=True, max_length=100)

    def get_absolute_url(self):
        return redirect('index')


    def approved_members(self):
        return self.bookings.filter(approved=True)

    class Meta():
        ordering = ['date', 'time']
    #
    # def set_admin(self):
    #     self.creator={{user.username}}



class Member(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='member_users', null=True)
    booking=models.ForeignKey('Booking', on_delete=models.CASCADE , related_name='members')
    name=models.CharField(max_length=90)
    

    def get_absolute_url(self):
        return reverse('index')



class Chat(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_users', null=True)
    booking=models.ForeignKey('Booking', on_delete=models.CASCADE , related_name='chats', null=True)
    name=models.CharField(max_length=90, null=True)
    message=models.CharField(max_length=500, null=True)
    photo=models.ImageField( null=True)
    time=models.TimeField(default=timezone.localtime)

    def get_absolute_url(self):
        return redirect('booking:chats_display', kwargs={'pk':self.booking.pk})


class Feedback(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbackers', null=True)
    feedback=models.CharField(max_length=500)
