from django.urls import path
from . import views


urlpatterns = [
	path('', views.LivingroomView.as_view(), name='livingroom')
]