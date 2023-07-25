from django.contrib import admin
from .models import Register, Rooms, Booking, FeedBack

# Register your models here.
admin.site.register(Register)
admin.site.register(Rooms)
admin.site.register(Booking)
admin.site.register(FeedBack)
