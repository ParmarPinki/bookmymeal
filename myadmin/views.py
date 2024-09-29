from django.shortcuts import render,redirect
from . import models
from django.core.files.storage import FileSystemStorage

def adminhome(request):
	return render(request,'adminhome.html',{})

def adminsettings(request):
	return render(request,'adminsettings.html',{})

def adminmanage(request):
	return render(request,'adminmanage.html',{})

def addcat(request):
	if request.method=='GET':
		return render(request,'addcat.html',{'output':''})	
	else:
		catnm=request.POST.get('catnm')
		caticon=request.FILES['caticon']
		fs = FileSystemStorage()
		filename = fs.save(caticon.name,caticon)
		
		query="insert into addcat values(NULL,'%s','%s')" %(catnm,filename)
		models.cursor.execute(query)
		models.db.commit()
		return render(request,'addcat.html',{'output':'Category Added Successfully'})



def addfood(request):
	query1="select * from addcat"
	models.cursor.execute(query1)
	clist=models.cursor.fetchall()

	if request.method=='GET':
		return render(request,'addfood.html',{'clist':clist,'output':''})	
	else:
		catnm=request.POST.get('catnm')
		foodnm=request.POST.get('foodnm')
		disc=request.POST.get('disc')
		price=request.POST.get('price')
		foodicon=request.FILES['foodicon']
		fs = FileSystemStorage()
		filename = fs.save(foodicon.name,foodicon)


		query="insert into addfood values(NULL,'%s','%s','%s',%s,'%s')" %(catnm,foodnm,disc,price,filename)
		models.cursor.execute(query)
		models.db.commit()
		return render(request,'addfood.html',{'clist':clist ,'output':'Food Added Successfully'})


def viewuser(request):
	query="select * from registertable where type='user'"
	models.cursor.execute(query)
	userDetails=models.cursor.fetchall()
	return render(request,'viewuser.html',{'userDetails':userDetails})


def manageuserstatus(request):
	regid=request.GET.get('regid')
	s=request.GET.get('s')
	
	if s=='block':
		query="update registertable set status=0 where regid=%s" %(regid)
	elif s=='unblock':
		query="update registertable set status=1 where regid=%s" %(regid)
	else:
		query="delete from registertable where regid=%s" %(regid)		

	models.cursor.execute(query)
	models.db.commit()
	return redirect('http://127.0.0.1:8000/myadmin/viewuser/')

