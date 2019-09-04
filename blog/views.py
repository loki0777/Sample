from blog.forms import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import  meUser



def home(request):
	return render(request, 'blogs/home.html')


def success(request):
    return render(request, 'blogs/success.html', {})

def login(request):
    return render(request, 'blogs/login.html', {})



def calcu(request):
	details = meUser.objects.all()
	return render(request, 'blogs/calcu.html', {'details': details})

def register(request):

	if request.method == "POST":
		print(request.POST.get('name'))
		data = {
		"name": request.POST.get('name'), 
		"email": request.POST.get('email'), 
		"password": request.POST.get('password'),
		"DD": request.POST.get('DD'),
		"MM": request.POST.get('MM'),
		"YYYY": request.POST.get('YYYY')}
		form = meUser_form(data)

		if form.is_valid():
			form.save()
			print('Save')
			messages.success(request, 'Student created successfully.')
			return redirect('calcu')
		else:
			print(form.errors)
			return render(request, 'blogs/register.html', data)


def remove_items(request):
	if request.method == 'POST':
		form = meUser_form()
		user = meUser.objects.all()
		item_id = int(request.POST.get('item_id'))
		item = meUser.objects.get(id=item_id)
		item.delete()
	return redirect('calcu')
		# context = {
		# "form": form,
		# "user": user
		# }
		# return render(request, "blogs/register.html", context)



