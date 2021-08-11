from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import RegisterForm,LoginForm

# Create your views here.
def login(request):
	if request.user.is_authenticated:
		return redirect('/client/dashboard')
	if request.method=="POST":
		form=LoginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user=auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request,user)
				return redirect('register')
			else:
				messages.error(request,'Invalid credentials')
				return render(request,'login.html',{'form':form})
		else:
			messages.error(request,'Invalid credentials')
			return render(request,'login.html',{'form':form})
	elif request.method=="GET":
		form=LoginForm()
		return render(request,'login.html',{'form':form})

def register(request):
	if request.user.is_authenticated:
		return redirect('/client/dashboard')
	if request.method=="POST":
		form=RegisterForm(request.POST)
		
		if form.is_valid():
			firstname=form.cleaned_data['firstname']
			lastname=form.cleaned_data['lastname']
			username=form.cleaned_data['username']
			email=form.cleaned_data['email']
			password1=form.cleaned_data['password1']
			password2=form.cleaned_data['password2']
			
			User.objects.create_user(first_name=firstname,last_name=lastname,email=email,password=password1,username=username).save()
			messages.info(request,"Registration successful")
			return redirect('login')
		else:
			return render(request,'register.html',{'form':form})
			
			
	elif request.method=="GET":
		form=RegisterForm()
		return render(request,'register.html',{'form':form})




