from django.shortcuts import render , redirect
from django.views.generic import ListView, TemplateView


# class SlotListView(ListView):

class IndexView(TemplateView):
    template_name='index.html'
