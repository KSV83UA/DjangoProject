from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Menu)
admin.site.register(Dishes)
admin.site.register(Sale)



class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_start', 'date_stop', 'is_visible']
    list_editable = ['is_visible']


class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date', 'time', 'message', 'count_of_people', 'status']
    list_editable = ['phone', 'date', 'time', 'message', 'count_of_people', 'status']


admin.site.register(Events, EventsAdmin)
admin.site.register(Clients, ClientsAdmin)

admin.site.register(Chief)



