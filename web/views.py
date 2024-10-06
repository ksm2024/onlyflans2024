from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm, Profile
from .forms import ContactFormForm, ContactModelForm, ProfileForm, UserForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
    

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        "mensaje": "Indice",
        "flanes_publicos": flanes_publicos
    }
    return render(request, 'index.html', context)

      
def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido (request):
    flanes_privados = Flan.objects.filter(is_private= True)
    return render(request, 'welcome.html', {"flanes_privados": flanes_privados})


def contacto(request):
    if request.method == 'POST':
        
        #* FORM
        form = ContactFormForm (request.POST) # <- {"customer_email": "kiki@gamial.com", "customer_name": "Kiki", "message": "Hola soy Kiki"}
        if form.is_valid():
            #* MODEL - Guardamos la data en nuestra DB en la TABLA CONACTFORM
            ContactForm.objects.create(**form.cleaned_data) # pasamos la data del diccionario .cleaned_data a argumentos
            return HttpResponseRedirect('/exito')
    else: 
        form = ContactFormForm ()    
    return render(request, 'contactus.html', {'form':form})



def exito(request):
    return render(request, 'exito.html', {})

def iniciar_sesion(request):
    return render(request, 'login.html', {})

def detalle_flan(request, flan_uuid):
    flan = Flan.objects.get(flan_uuid = flan_uuid)
    return render(request, 'detail_flan.html', {'flan' : flan})


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
    
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #* Se guarda el user en la DB
            login(request, user) #* Se logea
            return redirect('profile')  # Redirige a la vista de perfil u otra vista
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})