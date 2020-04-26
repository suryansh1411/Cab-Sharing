from django.shortcuts import render
from django.views.generic import CreateView , ListView, UpdateView , DeleteView
from bookings.models import Bookings
from bookings.forms import BookingForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class BookingsCreateView(LoginRequiredMixin, CreateView):
    model=Bookings
    form_class=BookingForm
    success_url=reverse_lazy('index')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(BookingsCreateView, self).form_valid(form)


class BookingsUpdateView(LoginRequiredMixin, UpdateView):
    model=Bookings
    form_class=BookingForm


class BookingsDeleteView(LoginRequiredMixin, DeleteView):
    model=Bookings
    success_url=reverse_lazy('index')


class BookingsListView( ListView):
    model=Bookings
    context_object_name='bookings_list'
