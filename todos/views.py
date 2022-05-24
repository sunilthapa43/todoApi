from django.http import Http404
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ListTodo(generics.ListAPIView):
    queryset =  Todo.objects.all()
    serializer_class =  TodoSerializer


"""class DetailsTodo(generics.ListAPIView):
  
    queryset =  Todo.objects.all()
    lookup_field = 'pk'
    serializer_class = TodoSerializer""" # so with accordance to the documentation generic views shall work with this chunk of code but there some problem with the views i guess so i had to use a class based views as alternative 

class DetailsTodo(APIView):

    def get_object(self,pk):
        try:
             return Todo.objects.get(pk = pk)
        except Todo.DoesNotExist: 
            raise Http404
    

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TodoSerializer(snippet)
        return Response(serializer.data)