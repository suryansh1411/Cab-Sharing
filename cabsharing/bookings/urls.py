from django.urls import path, re_path, include
from bookings import views
from django.conf.urls.static import static
from django.conf import settings
from chats import views as chat_views

app_name='bookings'

urlpatterns=[
    path('create/', views.BookingCreateView.as_view(template_name='bookings/bookings_form.html') , name='bookings_create'),
    re_path(r'^(?P<pk>\d+)/update/$', views.BookingUpdateView.as_view(template_name='bookings/bookings_update.html'), name='bookings_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.BookingDeleteView.as_view(template_name='bookings/bookings_delete.html'), name='bookings_delete'),
    re_path(r'^(?P<pk>\d+)/join/$', views.join_group , name='group_join'),
    re_path(r'^(?P<pk>\d+)/leave/$', views.leave_group , name='group_leave'),
    re_path(r'^(?P<pk>\d+)/info/$', views.GroupInfo.as_view(template_name='bookings/bookings_detail.html'), name='group_info'),
    # re_path(r'^(?P<pk>\d+)/chat/$', include('chats.urls', namespace='chats'), name='chats'),
    re_path(r'^(?P<pk>\d+)/chat/$', chat_views.PostListView.as_view(template_name='bookings/chat_list.html'), name='chat_list'),
    re_path(r'^(?P<pk>\d+)/post/$', chat_views.PostCreateView.as_view(template_name='bookings/chat_form.html'), name='message'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
