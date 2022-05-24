from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.IntegerField(primary_key=True, blank= False)
    title = models.CharField(max_length= 255)
    body= models.TextField()


    def __str__(self):
        return self.title