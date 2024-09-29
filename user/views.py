from django.shortcuts import render
from . import models
from django.conf import settings


curl=settings.CURRENT_URL

media_url=settings.MEDIA_URL

# Create your views here.
def userhome(request):
	return render(request,'userhome.html',{})
def usersettings(request):
	return render(request,'usersettings.html',{})

def placeorder(request):
	PAYPAL_URL="https://www.sandbox.paypal.com/cgi-bin/webscr"
	PAYPAL_ID="divyeshpandya2000-myseller@gmail.com"
	return render(request,'placeorder.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'pid':request.GET.get('pid'),'price':request.GET.get('price'),'PAYPAL_URL':PAYPAL_URL,'PAYPAL_ID':PAYPAL_ID})	
	
	



