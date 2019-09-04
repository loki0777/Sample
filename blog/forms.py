from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import *


class meUser_form(forms.ModelForm):
	class Meta():
		model = meUser
		fields = ('name','email','password','DD','MM','YYYY')



