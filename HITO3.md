### CARDS INSERTION DESDE BOOTSTRAP 
# OPCION A: MANUAL
1. EN TEMPLATE.PY IMPORTAR LAS CARDS NECESARIAS E INGRESAR INFORMACION MANUALMENTE

# OPCION B: CICLO FOR Y CONTEXT 
1. TEMPLATE.PY  USE FOR PARA CREAR UN LOOP CON FOR(SOLO SE NECESITA 1 CARD)

```PY
{% extends 'base.html' %} 
{% load static %}
{% block content %} 
<div class="container">
  
  <h1>{{message}}</h1>
  
  <div class="row row-cols-1 row-cols-md-3 g-4">
    {% for p in postres %}
    <div class="col-3">
      <div class="card">
        <img src="{{p.url}}" class="card-img-top" alt="Tarta de chocolate">
        <div class="card-body">
          <h5 class="card-title">{{p.name}}</h5>
          <p class="card-text">{{p.description}}</p>
        </div>
      </div>
    </div>
     {% endfor %} 
  </div>
  
</div>
{% endblock %}
```

2. VIEWS.PY
```PY
def index(req):
    context = {
        "message": "Indice",
        "postres": [
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-2.jpg?size=768x509&lossy=2&strip=1&webp=1",
                "name": "Tarta de chocolate",
                "description": "Una delicia que lleva dos planchas de bizcocho de chocolate, separadas por una fina capa de mermelada de damasco y recubiertas con un glaseado de chocolate."
            },
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-3.jpg?size=768x509&lossy=2&strip=1&webp=1",
                "name": "Tiramisú", 
                "description": "Bizcocho humedecido con una mezcla de café y licor y superponerlo en capas, alternando entre la crema y el bizcocho."
            },
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-4.jpg?size=768x512&lossy=2&strip=1&webp=1",
                "name": "Panna Cotta", 
                "description": "Parecido al flan y con una textura suave y gelatinosa."
            },
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-6.jpg?size=768x511&lossy=2&strip=1&webp=1",
                "name": "Pávlola", 
                "description": "Consiste en una base de merengue horneado sobre la cual se coloca crema batida, chocolate y trozos de fruta, en especial los frutos rojos."
            },
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-8.jpg?size=768x448&lossy=2&strip=1&webp=1",
                "name": "Crema de papaya", 
                "description": "Este postre está hecho a base de una crema de papaya y se acostumbra servirlo con helado de vainilla."
            },
            {
                "url": "https://b2844681.smushcdn.com/2844681/wp-content/uploads/2016/05/Sin-duda-probarlos-podr%C3%ADa-provocarte-una-muerte-deliciosa-pero-tranquilo-estos-postres-solo-te-alegrar%C3%A1n-la-vida-011.jpg?size=768x477&lossy=2&strip=1&webp=1",
                "name": "Milhojas", 
                "description": "Este crujiente postre está hecho de finas capas de masa hojaldre y lleva crema pastelera o crema de leche, tal vez ambos si eres fan del dulce y por encima está cubierto con azúcar impalpable."
            }
        ]  
    }  
    return render(req, 'index.html', context)
```

# OPCION 3: CICLO FOR Y DATABASE
# MODELS

1. Crear el Model -> models.py 
```PY
import uuid
from django.db import models
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
```

2. Register en admin.py

```PY
from django.contrib import admin
from .models import Flan

admin.site.register(Flan)

```

3. python manage.py makemigrations

Se crea un archivo en la carpeta migrations

4. python manage.py migrate

Se crea la Tabla equivalente a nuestro Model

5. Ingresar a la app como admin /admin   

6. Ir a la tabla FLAN ADD 8 flanes TRASPASANDO INFORMACION REQUERISA

7. Buscar data en nuestra db por medio del MODEL en VIEWS.PY
# BUSQUEDA DIRECTA
```py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan

def index(req):
    flanes_all = Flan.objects.all()
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(req, 'webtemp/index.html', {"flanes_publicos": flanes_publicos})
```
# BUSQUEDA POR CONTEXT
```PY
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan

def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        "mensaje": "hola",
        "flanes_publicos": flanes_publicos
    }
    return render(request, 'index.html', context)
```
8. EN TEMPLATE.PY HACER EL LINK {{}} CON LA INFORMACION REQURIDA USANDO LA KEY DE MODELS.PY

```PY
{% extends 'base.html' %} 
{% load static %}
{% block content %} 
<div class="container">
  
  <h1>{{message}}</h1>
  
  <div class="row row-cols-1 row-cols-md-3 g-4">
    {% for p in flanes_publicos %}
    <div class="col-3">
      <div class="card">
        <img src="{{p.image_url}}" class="card-img-top" alt={{p.name}}>
        <div class="card-body">
          <h5 class="card-title">{{p.name}}</h5>
          <p class="card-text">{{p.description}}</p>
        </div>
      </div>
    </div>
     {% endfor %} 
  </div>
  
</div>
{% endblock %}
```

### CONTACT FORM
0. AGREGAR EN NAVBAR
1. CREAR CONTACT.PY
```py
{% extends 'base.html' %} {% block content %}
<div class="container">
  <div class="col-12 col-md-6 offset-0 offset-md-3 mt-4 mb-4">
    <h3 class="text-center">Contáctanos</h3>

    <div>
      <form method="post">
       
        <button type="submit">Enviar</button>
      </form>

    </div>
  </div>
</div>
{% endblock %}
```
2. CREAR CLASS EN MODELS.PY
#FORMS.FORM
```PY
from django import forms
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name


```
- **Uso Típico**: Formularios para búsquedas, suscripciones, o entradas que no requieren persistencia en una base de datos.

# MODELS.FORM
 ```python
  from django import forms
  from .models import Contact

  class ContactModelForm(forms.ModelForm):
      class Meta:
          model = Contact
          fields = ['customer_email', 'customer_name', 'message']
  ```

- **Uso Típico**: Formularios para crear o editar instancias de modelos en la base de datos, como formularios de contacto, formularios de registro de usuario, o formularios de entrada de datos para una base de datos.


2. CREAR FUNCION EN VIEWS.PY
```PY
from .models import ContactForm

def contact(request):
    return render(request, 'contact.html', {})


# *  --- apply ContactModelForm ---
# from .forms import ContactModelForm  # Asegúrate de importar el formulario correcto

# *  <!-- apply MODEL-FORM contacto -->
def contacto_model_form(request):
    return render(request, 'contactus_model_form.html', {})
# *  --- apply ContactModelForm ---

3. CREAR RUTA EN URLS.PY

```
path('contact', views.contact),
```
