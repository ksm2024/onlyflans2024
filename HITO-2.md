# HITO-2

**HITO-2** Creación de un sitio web responsive con Bootstrap: en este Hito se crearán las primeras estructuras que permitirán mostrar datos en nuestro sitio web.

### Implementar

- **BOOTSTRAP**: Crear sitio web responsive con Bootstrap
- **STATIC**: Implementa un proyecto Django para servir contenido estático dando solución a los requerimientos. Implementar **load static a todo el documento** y marcar sintaxis de static cual: {% static 'path' %}
- **TEMPLATES**: Utiliza templates para la renderización de contenido dinámico en un proyecto Django para dar solución a un requerimiento.
  - VARIABLES
  - CONDICIONALES
  - HERENCIA: Utiliza herencia de plantillas en un proyecto Django para dar solución a un requerimiento. Django permite la reutilización de una plantilla dentro de otra.
  - LOOP (bucle FOR)
- **LOGIN-isActivate**: Utiliza instrucciones de control en plantillas de un proyecto Django para dar solución a un requerimiento.
  - Filtro if + | filter UPERCASE

---

### PASOS

1. Crear una plantilla o template base que tendrá los elementos comunes de la interfaz de nuestro sitio web OnlyFlans.
  - about
  - index
  - base
  - navbar
  - header
  - footer
  - welcome
  -contact


2. Habilitar las rutas o url: /, /acerca y /bienvenido, creando las vistas y plantillas necesarias que extiendan la plantilla base para mostrar diferentes contenidos para cada vista.

from django.urls import path 
from . import views
urlpatterns = [
    # path('text/', views.hola),
    path('', views.index),
    path('about/', views.acerca)
    # path('json/', views.hola_json),
    ]




3. Como elementos transversales mínimos que deberán mostrarse en todas las rutas se
   encuentran: - header, que contenga un logo para nuestra web - navbar, que permita la navegación entre las distintas rutas de nuestra web - footer, que entregue la información de “desarrollado por” incluyendo tu nombre y la frase “para Desafío Latam”, ejemplo: “desarrollado por Juan Perez para Desafío Latam”

4. Adicionalmente cada ruta deberá mostrar lo siguiente:
   - ruta /: deberá mostrar una lista de productos disponibles para la venta en la tienda de la PYME.
   - ruta /acerca: deberá mostrar una descripción de la utilidad del sitio web, junto con la descripción de la PYME y datos como la fecha de creación, entre otros que se dispongan.
   - ruta /bienvenido: deberá mostrar un mensaje de “bienvenido cliente” genérico en caso de no contar con los datos de un usuario y un mensaje de “bienvenido Juan Perez”(nombre variable) en el caso de contar con los datos del mismo.
urls.py

from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('text/', views.hola),
    path('', views.index, name= "indice"),
    path('acerca', views.acerca, name= "acerca"),
    path('bienvenido', views.bienvenido, name= "bienvenido"),
    # path('json/', views.hola_json),
    path('contacto', views.contacto, name="contacto"),
    path('exito', views.exito, name= "exito"),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




Para la mejor visualización del sitio web que estamos creando se debe utilizar tanto la “grilla” de bootstrap como sus componentes, permitiendo al sitio web “acomodarse” a distintos tamaños de pantalla y resoluciones, además de permitir su rápido desarrollo. Puedes valerte de componentes de bootstrap como navbar, tarjetas o cards, entre otros según desees.






## IMPORTANTE
Para mostrar los productos en el home (index.html nuestro) usamos una lista dentro del mismo views. 

# EXTRAS
- Ver como crear un model (+ migrate), como ver o eliminar datos desde el admin o como acceder a los datos de un modelo desde una view.
- Recordar como hacemos formularios como antes usando label, input y demás y ver como Forms de Django nos simplifica esto y nos brinda ya validaciones 




```
```

### SUPER EXTRAS
- Envío de email



-----------------------------------

Requerimientos
1. Inicia una nueva app de Django llamada web dentro del proyecto onlyflans y agrégala
a la lista de aplicaciones instaladas, dentro de ella crea una carpeta templates que
contenga un archivo html llamado index.html que contenga las estructuras <html>,
<header> y <body>. Dentro del <body> de este archivo escribe el texto “indice”.
Cree 2 copias del archivo index.html, llamadas about.html y welcome.html y reemplace
el texto de sus estructuras <body> por “acerca” y “bienvenido cliente”
respectivamente.
(1 Punto)
2. Habilitar las 3 urls distintas con un plantilla básica que muestre solo texto, esto
implica:
○ Mostrar el texto “índice” en la ruta /
○ Mostrar el texto “acerca” en la ruta /acerca
○ Mostrar el texto “bienvenido cliente” en la ruta /bienvenido
Una vez realizado esto, ejecuta el sitio web con python manage.py runserver, y crea un
“pantallazo” de cada una de esas rutas y guárdalas en formato jpg o png.
(1 Punto)
3. Crea una plantilla base llamada base.html que contenga los elementos comunes a
todas las rutas necesarias para el sitio web, esto puede ser, como en el caso anterior,
simplemente un texto que identifique cada elemento, por ejemplo:
○ Mostrar el texto “header” en el lugar donde iría el header
○ Mostrar el texto “navbar” en el lugar donde iría la barra de navegación
○ Mostrar el texto “footer” en el lugar donde iría el footer.
Debes valerte de estructuras como <div></div> para separar los distintos elementos,
y se recomienda agregarle un color de fondo a cada elemento para guiar de mejor
manera la estructura general de lo que estás maquetando, por ejemplo tu header
podria tener de color de fondo rojo utilizando lo siguiente:
<div style="background: red;">
 header
</div>
Los colores que se pueden utilizar son cualquier color html, ya sean por nombre(ejemplo:
green, yellow, red) o con código hexadecimal(ejemplo: #00ff00, #ffff00, #ff0000)
Una vez maquetado tu archivo base, extiendelo dentro de cada una de las rutas a
disponibilizar, respetando los textos agregados a cada una de las rutas en el texto anterior y
crea un “pantallazo” de cada una de ellas y guardalas en formato jpg o png.
(2 Puntos)
4. Crear las vistas y plantillas personalizadas, añadiendo componentes de bootstrap que
permitan crear un sitio más “rico” en cuanto al contenido, acercándose a lo requerido
en la descripción del presente hito, para esto debes realizar lo siguiente:
○ “Instala” bootstrap a través de incluir la “plantilla inicial” de bootstrap en el
plantilla base, complementando su estructura <body> con lo que ya existe en
el archivo. Luego de agregado esto, cambia el contenido de su estructura
<title> por “Bienvenido a onlyflans”.
Una vez realizado este cambio, debemos recargar la web, y en el título de la página
deberíamos ver algo como esto:
título pestaña de nuestra web
○ Al contenido de la web, en los <div> de header, navbar, contenido y footer
agrégale la clase css container, esto permitirá que el contenido de la web
quede en un espacio más acotado(centrado), y la posterior adaptación a
celulares del contenido cuando se use en conjunto con elementos que tengan
la clase css col. Este cambio debe aplicarse tanto en la plantilla base como en
aquellas plantillas que lo extienden.
Reemplaza los contenidos de header, navbar y footer por componentes de
bootstrap que te permitan darle más “estilo” a la web, se recomienda crear una
plantilla para cada componente(ejemplo: archivos header.html, navbar.html,
footer.html e incluirlos dentro de nuestra base utilizando la etiqueta include.
Algunos de los componentes de bootstrap que podrían serte útiles:
i. https://getbootstrap.com/docs/5.0/components/navbar/
ii. https://getbootstrap.com/docs/5.0/components/buttons/
iii. https://getbootstrap.com/docs/5.0/components/carousel/
iv. https://getbootstrap.com/docs/5.0/components/card/
El resultado de tu web ahora debería verse similar a esto
○ A cada elemento del navbar debes agregarle un enlace que permita dirigirte a
cada una de las url antes descritas al presionar sobre su respectivo nombre en
el navbar.
Una vez terminado lo anterior, crea un “pantallazo” de cada una de esas rutas y
guardalas en formato jpg o png.
(6 Puntos)
