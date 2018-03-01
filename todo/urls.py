from django.urls import path
from . import views


app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('complete_todo/<todo_id>', views.complete_todo, name='complete_todo'),
    path('delete_completed/', views.delete_completed, name='delete_completed'),
    path('delete_add/', views.delete_add, name='delete_add'),
]
