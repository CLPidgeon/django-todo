from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from todo.serializers import TodoSerializer
from todo.models import Todo
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.


class TodoView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        if "username" in request.query_params:
            if pk is None:
                user = User.objects.get(username=request.query_params["username"])
                todo_items = Todo.objects.filter(user=user)
                serializer = TodoSerializer(todo_items, many=True)
                serialized_data = serializer.data
                return Response(serialized_data)
            else:
                todo = Todo.objects.get(id=pk)
                serializer = TodoSerializer(todo)
                serialized_data = serializer.data
                return Response(serialized_data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):

        serializer = TodoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            user = User.objects.get(username=data["username"])
            Todo.objects.create(user=user, title=data["title"], description=data["description"], status=data["status"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):

        todo = Todo.objects.get(id=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

