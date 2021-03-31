from django.urls import path
from .import views
from .api import PizzaCreateApi, PizzaApi, PizzaUpdateApi,  PizzaDeleteApi

app_name = 'pizzaShop'

urlpatterns = [
	path('', views.home, name = 'home'),
	path('order/', views.order, name = 'order'),
	path('<int:detailId>/',views.detail, name = 'detail'),
	path('api',PizzaApi.as_view()),
	path('api/create',PizzaCreateApi.as_view()),
	path('api/<int:pk>',PizzaUpdateApi.as_view()),
	path('api/<int:pk>/delete',PizzaDeleteApi.as_view()),
]
