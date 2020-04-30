from django import forms
from bookings.models import Booking, Member, Chat

GENDER=[
    ('both boys and girls','both boys and girls'),
    ('girls only','girls only'),
    ('boys only', 'boys only')
]



class BookingForm(forms.ModelForm):
    start_position=forms.CharField(label='From:', required=True)
    destination=forms.CharField(label='To:', required=True)
    date=forms.DateField(label='Date:' ,required=True,widget=forms.DateInput() )
    time=forms.TimeField(label='Time:',required=True, widget=forms.TimeInput())
    max_members=forms.IntegerField(label='Maximum number of members:', help_text='maximum number of members includes you as well.', required=True)
    gender=forms.ChoiceField(label='Group open to:', choices=GENDER )


    class Meta():
        model=Booking
        fields=['start_position' ,'destination','date','time', 'max_members','gender']


class MemberForm(forms.ModelForm):

    class Meta():
        model=Member
        fields=[]


class MessageForm(forms.ModelForm):
    message=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Type a message'}))
    class Meta():
        model=Chat
        fields=['message']
