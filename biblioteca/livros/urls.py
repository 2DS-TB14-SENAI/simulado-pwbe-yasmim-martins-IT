from django.urls import path
from . import views


urlpatterns = [
     path('livros/', views.listaLivros) ,
     path('api/livros/', views.livros),
     path('api/livros/', views.livros)
]