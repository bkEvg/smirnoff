from django.urls import path
from . import views


urlpatterns = [
	path('', views.BedroomView.as_view(), name='bedroom'),
]