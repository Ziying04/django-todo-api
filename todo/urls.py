from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename='todo')

urlpatterns = [
    #path('',views.home),
    path('home/', views.home, name='Login'),
    path('create/', views.create_todo, name='create_todo'),
    #path('home/', include(router.urls))
]
