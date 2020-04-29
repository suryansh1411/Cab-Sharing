from django.contrib import admin
from bookings.models import Booking, Member, Chat
# Register your models here.
admin.site.register(Booking)
admin.site.register(Member)
admin.site.register(Chat)
