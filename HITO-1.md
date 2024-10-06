  1. Crea la carpeta onlyflans 
  2. Dentro de esta crea un entorno virtual
  python -m venv venv
  3. Activar 
  source venv/Scripts/activate
  4. Instala Django 
  pip install django==5.0.7 --trusted-host pypi.org --trusted-host files.pythonhosted.org
    pip freeze
  5. Crea un project con el llamado onlyflans (recuerden usar el punto al final) -->
  django-admin startproject onlyflans .
  6. Probar el Proyecto ejecutando runserver
  python manage.py runserver
  7. Preparar y migrar
  python manage.py makemigrations
  python manage.py migrate
  8. Crear user y password del admin
  python manage.py createsuperuser
  9. Probar el Proyecto ejecutando runserver e ingresar como admin
  /admin
  10. Crear una app llamada web
  python manage.py startapp web

  11. Armar la estructura
    - static
        - js index.js console.log(" ")
        - css index.css
        -favicon
        -img
    - templates index.html  / base.html
    - etc

  12. En la views.py de web crear una función de respuesta http 
  views.py en la app
from django.shortcuts import render
from django.http import HttpResponse
def hola(request):
  return HttpResponse("Hola, onlyflans")



  13. En la urls.py del proyecto anexar la route para la función previamente creada
urls.py en el project
from django.contrib import admin
from django.urls import path
from onlyflans.views import hola
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', hola)
]
  14. Modularizar la route creada (utilizando el include)
urls.py en el project
from django.contrib import admin
from django.urls import path, include
from web.views import hola

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hola),
    path('', include('web.urls')),
]
  15. Utiliza el utilitario manage.py para la creación de un nuevo proyecto Django.

  16. - .gitignore
  https://www.toptal.com/developers/gitignore/

  17. - README.md - Documentación

  18. - .env (variables de entorno)
  
  19. - requirements.txt
  pip freeze > requirements-onlyflans.txt
  20. Subir el proyecto a gitHub (privado)

-en la app agregar
  -URLS.PY 
-projecto settings.py
    -INSTALLED APP: agregar la/s app/s creadas
    'web'
    -STATIC: agregar
    import os
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
-.ENV (revisar repositorio)
 base

-tempaltes: html ---incluir arriba del link a css
{% load static %}

  href="{% static 'css/styles.css' %}"


21. TEMPLATES NO APARECIA Y DABA ERROR
en Settings.py 
import os
y agregar esta direccion --> [os.path.join(BASE_DIR, 'templates')]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

22. MOVER LA CARPETA TEMPLATES DENTRO DE LA APP WEB

# Requerimientos
1. python usada es python 3. Realiza un “pantallazo” de la versión de python mostrada en la terminal/consola y guardalo en un archivo jpg o png dentro de la carpeta requerimiento1.

2. Instalar django 3.2.4 dentro del entorno virtual onlyflans, una vez instalado verifica que 
haya sido instalado exitosamente utilizando el comando pip freeze. Realiza un 
“pantallazo” de la versión de python mostrada en la terminal/consola y guardalo en un 
archivo jpg o png dentro de la carpeta requerimiento2.

3. Usando django-admin genera un proyecto llamado onlyflans, una vez creado ingresa 
a la carpeta del proyecto generado, aplica las migraciones y ejecuta tu servidor 
utilizando los comandos correspondientes del archivo manage.py y accede a la url 
disponible para tu proyecto. Una vez que puedas acceder a la web en tu navegador, 
realiza un “pantallazo” de ésta y guardalo en un archivo jpg o png dentro de la carpeta
requerimiento3.
