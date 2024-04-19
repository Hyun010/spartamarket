from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields+()

class UserImageForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("image",)