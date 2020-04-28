from django import forms
from bookings.models import Booking, Member


class BookingForm(forms.ModelForm):
    start_position=forms.CharField(label='From:', required=True)
    destination=forms.CharField(label='To:', required=True)
    date=forms.DateField(required=True,widget=forms.DateInput() )
    time=forms.TimeField(required=True, widget=forms.TimeInput())
    max_members=forms.IntegerField(label='Maximum number of members:', help_text='maximum number of members includes you as well.', required=True)



    class Meta():
        model=Booking
        fields=['start_position' ,'destination','date','time', 'max_members']


class MemberForm(forms.ModelForm):

    class Meta():
        model=Member
        fields=[]
