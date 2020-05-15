from django.contrib import admin
from bookings.models import Booking, Member, Chat, Feedback
# Register your models here.
admin.site.register(Booking)
admin.site.register(Member)
admin.site.register(Chat)
admin.site.register(Feedback)
