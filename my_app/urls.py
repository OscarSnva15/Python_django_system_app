from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.inicio, name='inicio'),
    path('abouth/', views.abouth, name='nosotroa'),
    path('pagina/<int:redirigir>', views.pagina, name="pagina"),
    path('contactos-dos/', views.contactos, name="contacto"),
    path('contactos-dos/<str:nombre>', views.contactos, name="contacto"),
    path('contactos-dos/<str:nombre>/<str:apellidos>', views.contactos, name="contacto"),
]