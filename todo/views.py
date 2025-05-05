from django.shortcuts import render, redirect
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.todos.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['GET'])
def home(request):
    return Response(TodoItemSerializer(TodoItem.objects.all(), many=True).data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_todo(request):
    serializer = TodoItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



