from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import get_user_model
from django import forms

# from .models import User
User = get_user_model()


class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email']


class UserAdminForms(forms.ModelForm):
    class Meta:
        models = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']
