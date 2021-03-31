from django.shortcuts import render, get_object_or_404
from .models import Pizza
# Create your views here.

def home(request):
	pizza = Pizza.objects.all()
	return render(request, 'home.html', {'pizza': pizza})
	
def order(request):
	length = int(request.GET.get('length'))
	small1 = int(request.GET.get('small'))
	ammount = small1*length
	return render(request, 'order.html',{'ammount' : ammount})
	
def detail(request, detailId):
	pizza = get_object_or_404(Pizza, pk = detailId)
	return render(request, 'detail.html', {'pizza': pizza})
