from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserSignUpForm(UserCreationForm):
    first_name=forms.CharField(help_text='Enter Your First Name.')
    last_name=forms.CharField(help_text='Enter Your Last Name.')
    email=forms.EmailField()
    
    gen_op=(
        ('M','Male'),
        ('F','Female')
    )
    gender=forms.ChoiceField(choices=gen_op,initial='Male')
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','gender','password1','password2']

class UserUpdateForm(forms.ModelForm):
    first_name=forms.CharField(help_text='Enter Your First Name.')
    last_name=forms.CharField(help_text='Enter Your Last Name.')
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['first_name','last_name','username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']