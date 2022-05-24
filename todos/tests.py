from django.test import TestCase
from .models import Todo

# Create your tests here.


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title = 'first Todo', body = 'a body here')

    def test_title_content(self):
        todo = Todo.objects.get(id= 1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'first Todo')


    def test_body_content(self):
        todo =  Todo.objects.get(id= 1)
        expected_body = f'{todo.body}'
        self.assertEqual(expected_body, 'a body here')