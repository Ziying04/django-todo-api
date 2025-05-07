from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename='todo')

urlpatterns = [
    path('view/', views.view_todo, name='view_todo'),
    path('create/', views.create_todo, name='create_todo'),
    path('mark_completed/<int:pk>/', views.mark_todo_completed, name='mark_todo_completed'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    
]
