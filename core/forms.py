from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Item

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control form-control-lg'}), 
        label="")
    
    email = forms.EmailField(
        required=True, 
        widget=forms.widgets.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control form-control-lg'}), 
        label="")
    
    password1 = forms.CharField(
        required=True, 
        widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control form-control-lg'}), 
        label="")
    
    password2 = forms.CharField(
        required=True, 
        widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control form-control-lg'}), 
        label="")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'row': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'isSold')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'row': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
