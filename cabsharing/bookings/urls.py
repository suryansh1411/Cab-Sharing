from django.urls import path, re_path, include
from bookings import views
from django.conf.urls.static import static
from django.conf import settings

app_name='bookings'

urlpatterns=[
    path('create/', views.create_booking, name='bookings_create'),
    re_path(r'^(?P<pk>\d+)/update/$', views.update_booking, name='bookings_update'),

    # re_path(r'^(?P<pk>\d+)/update/$', views.BookingUpdateView.as_view(template_name='bookings/bookings_update.html'), name='bookings_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.BookingDeleteView.as_view(template_name='bookings/bookings_delete.html'), name='bookings_delete'),
    re_path(r'^(?P<pk>\d+)/join/$', views.join_group , name='group_join'),
    re_path(r'^(?P<pk>\d+)/leave/$', views.leave_group , name='group_leave'),
    re_path(r'^(?P<pk>\d+)/info/$', views.GroupInfo.as_view(template_name='bookings/bookings_detail.html'), name='group_info'),
    # re_path(r'^(?P<pk>\d+)/chats/$', views.MessageDisplayView.as_view(template_name='bookings/chats_list.html'), name='chats_display'),
    re_path(r'^(?P<pk>\d+)/chats/$', views.message_create, name='chats_display'),
    path('mybookings/', views.my_bookings, name='my_bookings'),
    # re_path(r'^(?P<pk>\d+)/my_bookings/$', views.mybooking, name='mybooking'),
    path('feedback/', views.feedback, name='feedback'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 