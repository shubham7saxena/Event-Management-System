from django.contrib import admin
from registeration.models import *
#from events.models import *

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(EventUserRegistration)