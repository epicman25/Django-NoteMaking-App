from django.shortcuts import render,redirect
from .models import Notes
from Notes.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate,logout
# Create your views here.
def createNote(request,reqId):
	if request.method == "POST":
		title = request.POST["title"]
		date = request.POST["date"]
		body = request.POST["body"]
		reqid = reqId
		Notes.objects.create(title=title,date=date,body=body,reqid = reqid)
		data = Notes.objects.filter(reqid = reqid)
		return render(request,"myApp/view-note.html",{"data":data,"d1":reqid})
	return render(request,"myApp/create-note.html",{"reqid":reqId})

def viewNote(request,reqId):
	data = Notes.objects.filter(reqid = reqId)
	if(len(data)>=1):
		d1 = data[0].reqid
	else:
		d1 = reqId	
	return render(request,"myApp/view-note.html",{"data":data,"d1":d1})

def deleteNote(request,Id):
	reqid = Notes.objects.get(id=Id).reqid
	Notes.objects.filter(id=Id).delete()
	data = Notes.objects.filter(reqid = reqid)

	return render(request,"myApp/view-note.html",{"data":data,"d1":reqid})

def update(request,Id):
	data = Notes.objects.get(id=Id)
	if request.method == "POST":
		title = request.POST["title"]
		date = request.POST["date"]
		body = request.POST["body"]
		Notes.objects.filter(id=Id).update(title=title,date=date,body=body)
		reqid = Notes.objects.get(id=Id).reqid
		data = Notes.objects.filter(reqid = reqid)
		return render(request,"myApp/view-note.html",{"data":data,"d1":reqid})
	return render(request,"myApp/edit-note.html",{"data":data})

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("view",user.id)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="myApp/register.html", context={"register_form":form})	

def login_req(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request , user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("view",user.id)
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="myApp/login.html", context={"login_form":form})

def signout(request):
    logout(request)
    return redirect("login")