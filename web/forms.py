from django import forms
from django.contrib.auth.models import User
from .models import ContactForm, Profile

class ContactFormForm(forms.Form):
    customer_name = forms.CharField(
        max_length=64,
        label='Nombre',
        widget=forms.TextInput(attrs={'placeholder': 'Introduce tu nombre'})
    )
    
    customer_email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce tu correo electrónico'})
    )
    
    phone_number = forms.CharField(
        max_length=20, 
        label='Teléfono',
        widget=forms.TextInput(attrs={'placeholder': 'Introduce tu número de teléfono'})
    )
    
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'placeholder': 'Introduce tu mensaje', 'rows': 4})
    )

class ContactModelForm (forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'phone_number', 'message']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Ingrese una dirección de correo electrónico válida.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email