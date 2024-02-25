from django.contrib import admin
from adminapi.models import user,Flight,Booking

# Register your models here.

admin.site.register(user)
admin.site.register(Flight)
admin.site.register(Booking)
