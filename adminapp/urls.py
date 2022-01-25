from django.urls import path
from . import views
urlpatterns=[
    path('loginpage/',views.fnlogin,name="loginpage"),
    path('masterpage/',views.fnmaster,name="masterpage"),
    path('homepage/',views.fnhome,name="homepage"),
    path('teampage/',views.fnteam,name="teampage"),
    path('clientpage/',views.fnclient,name="clientpage"),
    path('projectpage/',views.fnproject,name="projectpage"),
    path('salespage/',views.fnsales,name="salespage"),
    path('paymentpage/',views.fnpayment,name="paymentpage"),
    path('commentpage/',views.fncomment,name="commentpage"),


]