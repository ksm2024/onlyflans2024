
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
    path('detalle/<uuid:flan_uuid>', views.detalle_flan, name='detail_flan'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register, name='register'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

