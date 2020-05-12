from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView , ListView, UpdateView , DeleteView, DetailView
from bookings.models import Booking, Member, Chat
from bookings.forms import BookingForm, MemberForm, MessageForm, FilterForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import Http404
from django.contrib import messages
import datetime
# from datetime import timedelta
# Create your views here.

# User=get_user_model()
# class BookingCreateView(LoginRequiredMixin, CreateView):
#     model=Booking
#     form_class=BookingForm
#     success_url=reverse_lazy('index')
#
#     def form_valid(self, form):
#         form.instance.creator = self.request.user
#         return super().form_valid(form)
#
#     def save(self, *args, **kwargs):
#         if (self.gender == 'boys only' and (self.hostel=='Subhansiri' or self.hostel=='Dhansiri')):
#             messages.success(self.request, "A girl can't chose only boys option!")
#             return redirect('bookings:bookings_create')
#         elif (self.gender == 'girls only' and (not(self.hostel=='Subhansiri' or self.hostel=='Dhansiri'))):
#             messages.success(self.request, "A boy can't chose only girls option!")
#             return redirect('bookings:bookings_create')
#         else:
#             super().save(*args, **kwargs)
@login_required
def create_booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            booking=form.save(commit=False)

            if(booking.gender=='boys only'):
                if(request.user.userprofile.hostel=='Subhansiri' or request.user.userprofile.hostel=='Dhansiri'):
                    # messages.add_message(request, "A girl can't chose only boys option")
                    messages.success(request, "A girl can't chose <strong>only boys</strong> option")
                    return redirect('bookings:bookings_create')

            if(booking.gender=='girls only'):
                if(not(request.user.userprofile.hostel=='Subhansiri' or request.user.userprofile.hostel=='Dhansiri')):
                    # messages.add_message(request, "A girl can't chose only boys option")
                    messages.success(request,  "A boy can't chose <strong>only girls</strong> option")
                    return redirect('bookings:bookings_create')

            booking.user=request.user
            booking.creator=request.user.username
            booking.save()
            return redirect('index')
    else:
        form=BookingForm()
        return render(request, 'bookings/bookings_form.html', {'form':form})


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model=Booking
    form_class=BookingForm
    success_url=reverse_lazy('index')


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model=Booking
    success_url=reverse_lazy('index')
    success_message='Booking has been deleted'
    def delete(self, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(*args,**kwargs)

class BookingListView( ListView):
    model=Booking
    context_object_name='bookings_list'

    # def get_queryset(self):
    #     booking= Booking.objects.order_by('date')
    #     return booking.order_by('time')

@login_required
def my_bookings(request):
    context={}
    hehehe=[]
    context['mybooking']=Booking.objects.all().filter(creator__iexact=request.user.username)
    for booking in Booking.objects.all():
        for member in booking.members.all():
            if request.user.username == member.name:
                hehehe.append(booking)
    context['memberbooking']=hehehe
    return render(request, 'bookings/mybookings.html', context)


class GroupInfo(DetailView):
    model=Booking
    context_object_name='booking'
########################################################################################################
########################################################################################################


@login_required
def join_group(request, pk):
    booking=get_object_or_404(Booking, pk=pk)
    if request.method=='POST':
        form=MemberForm(request.POST)
        if form.is_valid():
            persons=booking.members.all()
            for person in persons:
                if(request.user.username == person.name):
                    messages.success(request,  "You are already a member of this Booking ")
                    return redirect('index')

            if (request.user.username==booking.creator):
                messages.success(request,  "You are already a member of this Booking ")
                return redirect('index')

            if(booking.gender=='boys only'):
                if(request.user.userprofile.hostel=='Subhansiri' or request.user.userprofile.hostel=='Dhansiri'):
                    messages.success(request,  "Girls can't join <strong>boys only</strong> bookings")
                    return redirect('index')

            if(booking.gender=='girls only'):
                if(request.user.userprofile.hostel=='Subhansiri' or request.user.userprofile.hostel=='Dhansiri'):
                    member=form.save(commit=False)
                    member.booking=booking
                    member.user=request.user
                    member.name=request.user.username
                    member.save()
                    messages.success(request,  "<strong> Booking </strong> joined successfully!")
                    return redirect('index')
                else:
                    messages.success(request,  "Boys can't join <strong> girls only </strong> bookings")
                    return redirect('index')


            member=form.save(commit=False)
            member.booking=booking
            member.user=request.user
            member.name=request.user.username
            member.save()
            messages.success(request,  "<strong> Booking </strong> joined successfully!")
            return redirect('index')


    else:
        form=MemberForm()
    return render(request, 'bookings/joining_form.html', {'form':form})



@login_required
def leave_group(request, pk):
    booking=get_object_or_404(Booking, pk=pk)
    if request.method=='POST':
        form=MemberForm(request.POST)
        if form.is_valid():
            try:
                member=booking.members.get(name=request.user.username)
                member.delete()
                messages.success(request,  "Booking left successfully! ")
                return redirect('index')
            except Member.DoesNotExist:
                messages.success(request,  "You are <strong> not</strong> a member of this Booking ")
                return redirect('index')
    else:
        form=MemberForm(request.POST)
    return render(request, 'bookings/leaving_form.html', {'form':form})

###########################################################################################
###########################################################################################
@login_required
def message_create(request, pk):
    booking=get_object_or_404(Booking, pk=pk)
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            chat=form.save(commit=False)
            chat.booking=booking
            chat.user=request.user
            chat.name=request.user.username
            chat.photo=request.user.userprofile.profile_pic
            chat.save()
        return redirect('bookings:chats_display', pk=booking.pk)
    else:
        form=MessageForm()
    return render(request, 'bookings/chats_form.html', {'form':form,
                                                        'booking':booking})



# def mybookings(request,pk):
###############################################################################################
###############################################################################################

@login_required
def filter(request):
    if request.method=='POST':
        form=FilterForm(request.POST)
        if form.is_valid():

            custom=Booking.objects.all()

            if(not (form.cleaned_data['start_position']=='')):
                custom=custom.filter(start_position__contains=form.cleaned_data['start_position'])
            if(not (form.cleaned_data['destination']=='')):
                custom=custom.filter(destination__contains=form.cleaned_data['destination'])
            if((form.cleaned_data['date'])):
                custom=custom.filter(date__iexact=form.cleaned_data['date'])
            if(form.cleaned_data['time']):
                time1=datetime.datetime.strptime(str(form.cleaned_data['time']), '%H:%M:%S')-datetime.timedelta(hours=1)
                time2=datetime.datetime.strptime(str(form.cleaned_data['time']), '%H:%M:%S')+datetime.timedelta(hours=1)
                custom=custom.filter(time__gte=time1)
                custom=custom.filter(time__lte=time2)
            custom=custom.filter(gender__iexact=form.cleaned_data['gender'])

            context={}
            context['custom']=custom
            return render(request, 'bookings/filter_display.html', context)
    else:
        form=FilterForm()
    return render(request, 'bookings/filter.html', {'form':form})
