import imp
from xmlrpc.client import ResponseError
from django.http import Http404, HttpResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
# Create your views here.


class ListTodo(generics.ListAPIView):
    queryset =  Todo.objects.all()
    serializer_class =  TodoSerializer
    

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            
            title =  serializer.validated_data.get('title')
            body =  serializer.validated_data.get('body')
            Todo.objects.create(title = title , body = body )
            msg = f'successfully added {title}'
            return Response({'message': msg})

            #serializer.save()

       

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


    
    def put(self, request, pk= None):
        return Response({'method': 'PUT'})
    
    def delete(self, request, pk= None):
        return Response({'method': 'DELETE'})
        
