from django import forms
from bookings.models import Bookings


class BookingForm(forms.ModelForm):
    # creator={{user.username}}
    start_position=forms.CharField(label='From:', required=True)
    destination=forms.CharField(label='To:', required=True)
    max_members=forms.IntegerField(label='Maximum number of members:', help_text='maximum number of members includes you as well.', required=True)
    # cab_timing=forms.DateTimeField(label='Cab Timing:', required=True)
    cab_timing=forms.CharField(label='Cab Timing:', required=True)


    class Meta():
        model=Bookings
        fields=['start_position' ,'destination','cab_timing', 'max_members']
