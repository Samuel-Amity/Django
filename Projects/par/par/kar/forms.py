from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,forms,PasswordResetForm,SetPasswordForm
from .models import Customer 
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':'True',
            "class":'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class RegistrationForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'autofocus' :'True',
                              'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='password',widget=forms.PasswordInput
                              (attrs={'class':'form-control'}))
    password2=forms.CharField(label='password',widget=forms.PasswordInput
                              (attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields= ['username','email','password1','password2']

class MyPasswordResetForm(PasswordResetForm):
    pass

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label='new password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label='Confirm New password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

# class CustomerProfileForm(forms.MOdelForm):
#     class Meta:
#         model=Customer
#         fields=['user','locality','city','mobile','state','zipcode']
#         widgets={
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             localitycitymibile state 

#         }
