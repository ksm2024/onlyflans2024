
1. Crear el Model Profile en el archivo models.py
```py
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # -> asocición - relación
    bio = models.TextField(max_length=500, blank=True) # el campo puede estar vacío
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True) # generalmente YYYY-MM-DD (por ejemplo, 2024-08-17).

    def __str__(self):
        return self.user.username
```
2. python manage.py makemigrations
3. python manage.py migrate
4. Anexar al admin.py 
```py
from django.contrib import admin
from .models import Flan, ContactForm, Profile
admin.site.register(ContactForm)
admin.site.register(Flan)
admin.site.register(Profile)
```
5. Crear los FORMS - ProfileForm & UserForm en archivo forms.py 
```py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

#* PROFILE FORMS 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
# ---
```
6. Crear Vista profile_view en archivo views.py 
```py 
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    # Verificar que el User tiene un Perfil 
    user_id = request.user.id 
    
    user = request.user
    #* User de no tener un Profile, crea la relación
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
        profile = Profile.objects.get(user_id=user_id)
        print(f'user profile get -> {profile.__dict__}')
        
    #* ARMADO POST - crea (guarda en la tabla) - y redirect
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Redirigir a la misma página después de guardar
            return redirect('/bienvenido')
    #* GET FORM - Creamos los forms con los datos de la DB de ese user
    else: 
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
```
7. Crear el template (la plantilla) profile.html 
```html 
{% extends 'base.html' %} 

{% block content %}
<div class="d-flex flex-column min-vh-100 bg-light">
    <div class="row justify-content-center align-items-center" style="height: 100vh;">
        <div class="col-md-8">
            <!-- Contenido centrado horizontal y verticalmente -->
            <h2 class="text-center mt-2 mb-4">Perfil</h2>
            <form method="post">
                {% csrf_token %}
                <div class="row">
                    <div class="col-md-6">
                        <!-- <h4>Información del Usuario</h4> -->
                        <!-- Personalizamos el formulario del usuario directamente -->
                        <div class="mb-3">
                            <label for="{{ user_form.first_name.id_for_label }}" class="form-label">Nombre</label>
                            {{ user_form.first_name }}
                        </div>
                        <div class="mb-3">
                            <label for="{{ user_form.last_name.id_for_label }}" class="form-label">Apellido</label>
                            {{ user_form.last_name}}
                        </div>
                        <div class="mb-3">
                            <label for="{{ user_form.email.id_for_label }}" class="form-label">Email</label>
                            {{ user_form.email}}
                        </div>
                    </div>

                    <div class="col-md-6">
                        <!-- <h4>Información del Perfil</h4> -->
                        <!-- Personalizamos el formulario del perfil directamente -->
                        <div class="mb-3">
                            <label for="{{ profile_form.bio.id_for_label }}" class="form-label">Biografía</label>
                            {{ profile_form.bio}}
                        </div>
                        <div class="mb-3">
                            <label for="{{ profile_form.location.id_for_label }}" class="form-label">Ubicación</label>
                            {{ profile_form.location}}
                        </div>
                        <div class="mb-3">
                            <label for="{{ profile_form.birth_date.id_for_label }}" class="form-label">Fecha de Nacimiento (YYYY-MM-DD)</label>
                            {{ profile_form.birth_date}}
                        </div>
                    </div>
                </div>

                <div class="mt-3 text-end">
                    <button type="submit" class="btn btn-primary">Guardar Cambios</button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```
8. Incorporar la ROUTE (el path) en el archivo de app web urls.py 
```py 
path('profile/', views.profile_view, name='profile'),
```

### **TESTEAR** 
Para probar el funcionamiento de esta vista deben estar logeados