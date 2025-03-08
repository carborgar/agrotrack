from django.urls import path

from . import views
from .views import TaskListView

urlpatterns = [
    path("", views.FieldListView.as_view(), name="field_list"),  # Listado de parcelas
    path('tareas/', TaskListView.as_view(), name='task_list'),  # Listado de tareas

]
