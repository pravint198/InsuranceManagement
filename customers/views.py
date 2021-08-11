from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from customers.forms import CustomerForm,PolicyForm
from .models import Customers, Policies
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import Http404
# Create your views here.

def addCustomer(request):
	if not request.user.is_authenticated:
		return redirect('/accounts/login')

	
	if request.method=='POST':
		form=CustomerForm(request.POST)
		if form.is_valid():
			Customers(name=form.cleaned_data['name'],father_name=form.cleaned_data['father_name'],mother_name=form.cleaned_data['mother_name'],spouse_name=form.cleaned_data['spouse_name'],gender=form.cleaned_data['gender'],is_married=form.cleaned_data['is_married'],dob=form.cleaned_data['dob'],place_of_birth=form.cleaned_data['place_of_birth'], correspondence_address=form.cleaned_data['correspondence_address'],is_perm_same=form.cleaned_data['is_perm_same'],permanent_address=form.cleaned_data['permanent_address'],pan=form.cleaned_data['pan'],aadhar=form.cleaned_data['aadhar'],education=form.cleaned_data['education'],mobile=form.cleaned_data['mobile'],height=form.cleaned_data['height'],weight=form.cleaned_data['weight'],username=request.user.username).save()
			#form.save()
			messages.info(request,'Customer saved successfully',extra_tags='text-success')
			return redirect('/client/add')
		else:
			messages.error(request,'Correct all the errors',extra_tags='text-danger')
			return render(request,'addClient.html',{'form':form})
	elif request.method=='GET':
		form=CustomerForm()
		return render(request,'addClient.html',{'form':form})

def logout(request):
	auth.logout(request)
	return redirect('/')

def dashboard(request):
	if not request.user.is_authenticated:
		return redirect('/accounts/login')
	if request.method=='GET':
		if(request.user.is_superuser):
			custs=Customers.objects.order_by('id').all()
		else:
			custs=Customers.objects.order_by('id').filter(username=request.user.username)
		return render(request,'dashboard.html',{'custs':custs})



def modifyCustomer(request,cust_id):
	if not request.user.is_authenticated:
		return redirect('/accounts/login')
	if request.method=='GET':		
		if(request.user.is_superuser):
			cust=get_object_or_404(Customers, pk=cust_id)#Customers.objects.get(pk=cust_id)
		else:
			cust=get_object_or_404(Customers, pk=cust_id, username=request.user.username)#Customers.objects.get(pk=cust_id)
		form=CustomerForm(instance=cust)
		return render(request,'addClient.html',{'form':form,'cust_id':cust_id,'is_modify':True})
			
	if request.method=='POST':
		#cust_id=request.POST.get('id')
		#if not cust_id is None:
		if(request.user.is_superuser):
			instance=get_object_or_404(Customers, pk=cust_id)#Customers.objects.get(pk=cust_id)
		else:
			instance=get_object_or_404(Customers, pk=cust_id, username=request.user.username)#Customers.objects.get(pk=cust_id)
		#instance=Customers.objects.get(pk=cust_id)
		form=CustomerForm(request.POST or None,instance=instance)
		if form.is_valid():
			form.save()
			messages.info(request,'Customer saved successfully',extra_tags='text-success')
			return redirect('/client/modify/'+str(cust_id))
			#return render(request,'addClient.html',{'form':form,'is_modify':True,'id':cust_id})
		else:
			messages.error(request,'Correct all the errors',extra_tags='text-danger')
			return render(request,'addClient.html',{'form':form,'is_modify':True,'cust_id':cust_id})
	

def addPolicy(request,cust_id):
	if not request.user.is_authenticated:
		return redirect('/accounts/login')

	
	if request.method=='POST':
		
		form=PolicyForm(request.POST)
		if form.is_valid():
			form.save()
			messages.info(request,'Policy saved successfully',extra_tags='text-success')
			return redirect('/client/policy/add/'+str(cust_id))
		else:
			messages.error(request,'Correct all the errors',extra_tags='text-danger')
			return render(request,'policy.html',{'form':form,'cust_id':cust_id})
	elif request.method=='GET':
		if Customers.objects.filter(pk=cust_id,username=request.user.username) or request.user.is_superuser:
			data = {'cid': cust_id}
			form=PolicyForm(initial=data)
			return render(request,'policy.html',{'form':form,'cust_id':cust_id})
		else:
			raise Http404("You are not authorized")
			



def showPolicies(request,cust_id):
	if not request.user.is_authenticated:
		return redirect('/accounts/login')
	if request.method=='GET':
		if Customers.objects.filter(pk=cust_id,username=request.user.username) or request.user.is_superuser:
			policies=Policies.objects.order_by('id').filter(cid=cust_id)
			return render(request,'show_policies.html',{'policies':policies,'cust_id':cust_id})
		else:
			raise Http404("This customer is not associated with logged user")

def deletePolicy(request,policy_id):
	if not request.user.is_authenticated:
		return redirect('/accounts/login')
	if request.method=='GET':
		
		policy=Policies.objects.get(id=policy_id)
		cust_id=policy.cid_id
		print(cust_id)
		if request.user.is_superuser or Customers.objects.filter(pk=cust_id,username=request.user.username):
			policy.delete()
			policies=Policies.objects.order_by('id').filter(cid=cust_id)
			return redirect('/client/policy/show/'+str(cust_id))
		else:
			raise Http404("This customer is not associated with logged user")
		