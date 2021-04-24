from django.shortcuts import render
from rest_framework import generics, status
from .models import Libro
from .serializer import LibroSerializer
from rest_framework.response import Response
from django.http import Http404

# Create your views here.
class LibroList(generics.ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class LibroCreate(generics.CreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    


class LibroUpdate(generics.UpdateAPIView):
    serializer_class = LibroSerializer
    def get(self, request, pk, format=None):
        libro = self.get_object(pk)
        serializer = LibroSerializer(libro)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        libro = self.get_object(pk)
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            raise Http404


class LibroDelete(generics.DestroyAPIView):
    serializer_class = LibroSerializer
    def delete(self, request, pk, format=None):
        libro = self.get_object(pk)
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            raise Http404
