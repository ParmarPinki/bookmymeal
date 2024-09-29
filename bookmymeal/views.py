from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from . import models 
import time
from django.views.decorators.csrf import csrf_protect

curl=settings.CURRENT_URL

media_url=settings.MEDIA_URL


def home(request):
	query="select * from addcat"
	models.cursor.execute(query)
	clist=models.cursor.fetchall()
	return render(request,'index.html',{'curl':curl,'media_url':media_url,'clist':clist})

def contact(request):
	return render(request,'contact.html',{})

def service(request):
	return render(request,'service.html',{})
@csrf_exempt
def login(request):
	if request.method=='GET':
		return render(request,'login.html',{'curl':curl,'output':''})
	else:
		email=request.POST.get('email')
		password=request.POST.get('password')
		print(email)
		
		
		query= "select * from registertable where email='%s' and password='%s' "%(email,password)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		print(userDetails)
		# models.cursor.close()
		
		if len(userDetails)>0:
			if userDetails[0][8]=='user':
				return redirect('http://127.0.0.1:8000/user/')
			else:
				return redirect('http://127.0.0.1:8000/myadmin/')	
		else:
			return render(request,'login.html',{'curl':curl,'output':'Login failed, invalid user or verify your account'})	
	# return render(request,'login.html',{})

	# email=request.POST.get('email')
	# password=request.POST.get('password')

	# query="select * from registertable where email='%s' && password='%s'"%(email,password)
	# models.cursor.execute(query)
	



	# return render(request,'userhome.html',{})

# @ensure_csrf_cookie
@csrf_protect
def register(request):
	if request.method=='GET':
		return render(request,'register.html',{'curl':curl,'output':''})
	else:
		name=request.POST.get('name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		address=request.POST.get('address')
		mobile=request.POST.get('mobile')
		city=request.POST.get('city')
		gender=request.POST.get('gender')
		dt=time.asctime(time.localtime(time.time()))
		
		query="insert into registertable values(NULL,'%s','%s','%s','%s','%s','%s','%s','user',0,'%s')" %(name,email,password,address,mobile,city,gender,dt)
		models.cursor.execute(query)
		models.db.commit()
		
		return render(request,'register.html',{'curl':curl,'output':'Registration successfull....'})

def viewsubcat(request):
	query1="select * from addcat"
	models.cursor.execute(query1)
	clist=models.cursor.fetchall()

	cnm=request.GET.get('cnm')
	query="select * from addfood where catnm='%s' " %(cnm)
	models.cursor.execute(query)
	sclist=models.cursor.fetchall()
	return render(request,'viewsubcat.html',{'curl':curl,'media_url':media_url,'sclist':sclist,'clist':clist,'cnm':cnm})

@csrf_exempt	
def orderlogin(request):
	if request.method=="GET":
		pid=request.GET.get('pid')
		price=request.GET.get('price')
		return render(request,"orderlogin.html",{'curl':curl,'pid':pid,'price':price})	
	else:
		email=request.POST.get('email')
		password=request.POST.get('password')
		pid=request.POST.get('pid')
		price=request.POST.get('price')
		
		query="select * from registertable where email='%s' and password='%s' and status=0 " %(email,password)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		
		
		if len(userDetails)>0:
			response=redirect(curl+'user/placeorder/?pid='+str(pid)+"&price="+str(price))
			response.set_cookie('cunm',email,3600*24)
			return response		
		else:
			return render(request,'orderlogin.html',{'curl':curl,'output':'Invalid user or verify your account to order product'})
	

def viewfood(request):
	query1="select * from addcat"
	models.cursor.execute(query1)
	sclist=models.cursor.fetchall()	

	scnm=request.GET.get('scnm')
	sprice=request.GET.get('sprice')
	eprice=request.GET.get('eprice')

	query="select * from addfood where catnm='%s' " %(scnm)
	
	# if sprice==None: 
	# 	query="select * from addfood where catnm='%s' " %(scnm)
	# else:
	# 	query="select * from addfood where catnm='%s' and price between %s and %s" %(scnm,int(sprice),int(eprice))	
	
	models.cursor.execute(query)
	fplist=models.cursor.fetchall()
	print(fplist)
	return render(request,'viewfood.html',{'curl':curl,'media_url':media_url,'fplist':fplist,'sclist':sclist,'scnm':scnm,'total':len(fplist)})	

