"""mysite_project URL Configuration

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
from django.urls import path, include 
# from my_app.views import hello

# ya no necesito llamar las views acorde pues sería no practico realizar un buen de llamadas para cada aplicacion
# from my_app import views

"""definir las url's que los usuarios podran estar visistando, 
    y en estas direcciones haran que se manden a llamar
    determinadas funciones
"""

#importar app. con mis vistas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls'))
]
