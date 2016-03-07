from django.contrib import admin
from registeration.models import *

class EventAdmin(admin.ModelAdmin):
	list_display = ('name','event_coordi','contact_id_coordinator','participants_list',)
	list_filter = ('name','event_coordi',)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('UserName','Email','phone',)
	list_filter = ('user',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Event,EventAdmin)