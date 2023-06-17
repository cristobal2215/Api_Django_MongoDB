from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Estudiante
from .serializer import EstudianteSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET','POST'])#decorador tomalos metodos a los que debe responder 
def EstudianteApiView(request):
    if request.method == 'GET':
        snippets = Estudiante.objects.all()
        serializer = EstudianteSerializer(snippets,many=True)#Llegaran muchos datos desde serializador desde una lista,"all"
        return Response(serializer.data) 
    elif request.method == 'POST':
        serializer = EstudianteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET",'PUT','DELETE'])
def EstudianteDetalle(request, pk):
    try:
        snippet = Estudiante.objects.get(pk=pk)
    except Estudiante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#no se encuentra
    if request.method == 'GET':
        serializer = EstudianteSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EstudianteSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
