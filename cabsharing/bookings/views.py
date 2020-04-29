from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView , ListView, UpdateView , DeleteView, DetailView
from bookings.models import Booking, Member, Chat
from bookings.forms import BookingForm, MemberForm, MessageForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
# Create your views here.


class BookingCreateView(LoginRequiredMixin, CreateView):
    model=Booking
    form_class=BookingForm
    success_url=reverse_lazy('index')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(BookingCreateView, self).form_valid(form)


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model=Booking
    form_class=BookingForm
    success_url=reverse_lazy('index')


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model=Booking
    success_url=reverse_lazy('index')


class BookingListView( ListView):
    model=Booking
    context_object_name='bookings_list'

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
                    return redirect('index')

            if (request.user.username==booking.creator):
                return redirect('index')

            member=form.save(commit=False)
            member.booking=booking
            member.name=request.user.username
            member.save()
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
                return redirect('index')
            except Member.DoesNotExist:
                return redirect('index')
    else:
        form=MemberForm(request.POST)
    return render(request, 'bookings/leaving_form.html', {'form':form})

###########################################################################################
###########################################################################################

def message_create(request, pk):
    booking=get_object_or_404(Booking, pk=pk)
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            chat=form.save(commit=False)
            chat.booking=booking
            chat.name=request.user.username
            chat.photo=request.user.userprofile.profile_pic
            chat.save()
        return redirect('bookings:chats_display', pk=booking.pk)
    else:
        form=MessageForm()
    return render(request, 'bookings/chats_form.html', {'form':form})

class MessageDisplayView(LoginRequiredMixin, DetailView):
    model=Booking
    context_object_name='booking'
