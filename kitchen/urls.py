from django.urls import path
from . import views 

urlpatterns = [
	path('', views.KitchenView.as_view(), name='kitchen')
]