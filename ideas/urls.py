from django.urls import path
from . import views


urlpatterns = [
	path('', views.IdeasView.as_view(), name='ideas_list'),
	path('<int:pk>/', views.IdeasDetailView.as_view(), name='ideas_detail')
]