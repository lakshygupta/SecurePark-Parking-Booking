from django.urls import path
from .import views

urlpatterns = [
path('', views.home, name='home'),
path('index/', views.index, name='index'),
path('entryex/', views.entryex, name='entryex'),
path('signup/', views.signup, name='signup'),
path('forgot/', views.forgot, name='forgot'),
path('vehicleentry/', views.vehicleentry, name='vehicleentry'),
path('aboutus/', views.aboutus, name='aboutus'),
path('complaint/', views.complaint, name='complaint'),
path('fare/', views.fare, name='fare'),
path('maps/', views.maps, name='maps'),
path('vehicleexit/', views.vehicleexit, name='vehicleexit'),
path('contactus/', views.contactus, name='contactus'),
path('printentry/', views.printentry, name='printentry'),
path('printexit/', views.printexit, name='printexit'),
path('printcontact/', views.printcontact, name='printcontact'),
path('printcomplaint/', views.printcomplaint, name='printcomplaint'),
path('adminpage/', views.adminpage, name='adminpage'),
path('printvehicles/', views.printvehicles, name='printvehicles'),
path('searchingveh/<vnumber>', views.searchingveh, name='searchingveh'),
]