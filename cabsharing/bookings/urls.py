from django.urls import path, re_path
from bookings import views


app_name='bookings'

urlpatterns=[
    path('create/', views.BookingsCreateView.as_view(template_name='bookings/bookings_form.html') , name='bookings_create'),
    re_path(r'^(?P<pk>\d+)/update/$', views.BookingsUpdateView.as_view(template_name='bookings/bookings_update.html'), name='bookings_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.BookingsDeleteView.as_view(template_name='bookings/bookings_delete.html'), name='bookings_delete'),

]
