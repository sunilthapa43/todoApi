from django.urls import path
from .views import ListTodo, DetailsTodo

urlpatterns = [
   
    path('', ListTodo.as_view()),
    path('<int:pk>/',DetailsTodo.as_view()),
   
]