from django.shortcuts import render

# Create your views here.
def fnlogin(req):
    return render(req,'adminlogin.html')
def fnmaster(req):
    return render(req,'adminmaster.html') 
def fnhome(req):
    return render(req,'adminhome.html') 
def fnteam(req):
    return render(req,'adminteam.html')    
def fnclient(req):
    return render(req,'adminclient.html')    
def fnproject(req):
    return render(req,'adminproject.html')    
def fnsales(req):
    return render(req,'adminsales.html')    
def fnpayment(req):
    return render(req,'adminpayment.html')    
def fncomment(req):
    return render(req,'admincomment.html')                            