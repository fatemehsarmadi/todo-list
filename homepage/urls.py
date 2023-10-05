from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_tasks, name='index'),
    path('add-task/', views.add_task, name='add_task'),
    path('toggle/', views.toggle_task_status, name='toggle_task_status'),
    path('delete/', views.delete_task, name='delete_task'),
    path('update/', views.update_task, name='update_task'),
    path('done/', views.save_update, name = 'save_update'),
    path('add/', views.add_deadline, name = 'add_deadline'),
]