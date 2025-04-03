from django.shortcuts import render
from .models import Livro
from rest_framework.decorators  import api_view 
from rest_framework.response import Response 
from rest_framework.request import Request
from .serializers import LivroSerializer
from rest_framework import status



@api_view(['GET','POST'])
def livros (request):
    if request.method == 'GET':
    
        livros = Livro.objects.all().order_by('-titulo')

        serializer = LivroSerializer(livros , many = True)

        return Response(serializer.data , status= status.HTTP_200_OK)

    
    elif request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def listaLivros(request) :
    livros = Livro.objects.all().order_by('-titulo')
    return render(request,'livro/listaLivros.html', {'livros' : livros})

# Create your views here.
