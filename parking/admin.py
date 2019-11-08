from django.contrib import admin

# Register your models here.
from .models import Registration
from .models import Contact
from .models import Complaints
from .models import Vehicleentry
from .models import Vehicleexit

admin.site.register(Registration)
admin.site.register(Contact)
admin.site.register(Complaints)
admin.site.register(Vehicleentry)
admin.site.register(Vehicleexit)
