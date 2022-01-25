from django.shortcuts import render

# Create your views here.
def fnmaster(req):
    return render(req,'master.html')
def fnhome(req):
    return render(req,'home.html')
def fncontact(req):
    return render(req,'contact.html')
def fnabout(req):
    return render(req,'about.html')
def fnservices1(req):
    return render(req,'business.html')
def fnservices2(req):
    return render(req,'hr.html') 
def fnservices3(req):
    return render(req,'marketing.html')       
def fnworkwith(req):
    return render(req,'work.html')
