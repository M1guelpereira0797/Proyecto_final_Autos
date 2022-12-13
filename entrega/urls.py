"""entrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from familia.views import index,  mostrar_familiar, buscar_familiar, AltaFamiliar, Actualizafamilia, familiaCrear, familialist, familiaBorrar 
###from blog.views import index as blog_index

urlpatterns =[
      path('admin/', admin.site.urls),
      path('familia/', mostrar_familiar), 
      path('buscar_familia',  buscar_familiar.as_view()),
      path('Alta_Familia', AltaFamiliar.as_view()),
      path('Actualizar_Familia/<int:pk>', Actualizafamilia.as_view()),
       path('Lista_de_Familiares/', familialist.as_view()), 
      path('Crear_Familiar', familiaCrear.as_view()),
      path('Borrar_Familiar/<int:pk>/borrar', familiaBorrar.as_view()), 
      path('Actuazlizar_dato_familiar /<int:pk>/actualizar', Actualizafamilia.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR

  ]
  
 