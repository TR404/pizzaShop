from django.shortcuts import render, redirect, get_object_or_404
#from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate 
from .models import Pizza
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	return render(request, 'pizzaShop/home.html')

@login_required	
def index(request):
	pizza = Pizza.objects.all()[::-1]
	return render(request, 'pizzaShop/index.html', {'pizza': pizza})
	
def signupuser(request):
	if request.method == 'GET':
		return render(request, 'pizzaShop/signupuser.html', {'form': UserCreationForm})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('index')
			except IntegrityError:
				return render(request, 'pizzaShop/signupuser.html', {'form': UserCreationForm(), 'error': 'Username already taken Plese choose different username'})
		else:
			return render(request, 'pizzaShop/signupuser.html', {'form': UserCreationForm(), 'error': 'Password did not match.'})
			
			
def loginUser(request):
	if request.method == 'GET':
		return render(request, 'pizzaShop/loginUser.html', {'form': AuthenticationForm()})
	else:
		user = authenticate(request, username =request.POST['username'] , password = request.POST['password'])
		if user is None:
			return render(request, 'pizzaShop/loginUser.html', {'form': AuthenticationForm(), 'error': 'username and password are not matching.'})
		else:
			login(request, user)
			return redirect('index')
			
@login_required	
def logoutUser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('index')
	

def order(request):
	length = int(request.GET.get('length'))
	small1 = int(request.GET.get('small'))
	ammount = small1*length
	return render(request, 'pizzaShop/order.html',{'ammount' : ammount})
	
@login_required	
def detail(request, detailId):
	pizza = get_object_or_404(Pizza, pk = detailId)
	return render(request, 'pizzaShop/detail.html', {'pizza': pizza})
