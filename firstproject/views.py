from django.shortcuts import render,redirect

# Create your views here.
def home(request):
	if request.user.is_authenticated:
		return redirect('/client/dashboard')
	else:
		return render(request,'index.html')


