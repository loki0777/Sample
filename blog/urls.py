from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^home$', views.home, name='home'),
	url(r'^register$', views.register, name='register'),
	url(r'^success$', views.success, name='success'),
	url(r'^login$', views.login, name='login'),
	url(r'^calcu$', views.calcu, name='calcu'),
	url(r'^remove_items/', views.remove_items, name='remove_items'),

    
]