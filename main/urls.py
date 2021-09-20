from django.urls import path 
from . import views

urlpatterns = [
	path('', views.MainPageView.as_view(), name='main'),
	path('language/activate/<lang_code>/', views.ActivateLanguageView.as_view(), name='activate_language'),
	path('create-proposal/', views.form_handler, name='create_proposal')
]