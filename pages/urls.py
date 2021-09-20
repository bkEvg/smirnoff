from django.urls import path
from . import views


urlpatterns = [
	path('<slug>/', views.PageView.as_view(), name='page')
]