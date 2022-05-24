from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Todo
        fields = '__all__'




    

#problem: not serializable 
#resolved 
#might be: 1. restarting vs code  2. re-writing serializers.py 
        