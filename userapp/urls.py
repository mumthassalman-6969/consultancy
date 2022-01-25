from django.urls import path
from . import  views
urlpatterns=[
    path('master/',views.fnmaster,name="master"),
    path('homepage/',views.fnhome,name="homepage"),
    path('contact/',views.fncontact,name="contact"),
    path('about/',views.fnabout,name="about"),
    path('businessconsulting/',views.fnservices1,name="businessconsulting"),
    path('hrconsulting/',views.fnservices2,name="hrconsulting"),
    path('marketing/',views.fnservices3,name="marketing"),
    path('workwith/',views.fnworkwith,name="workwith"),
    
]