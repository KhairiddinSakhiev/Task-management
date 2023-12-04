# urls.py
from django.urls import path
from .views import TasksCreateView, TaskListView, TaskUpdateView, TaskDetailView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
    path('create/', TasksCreateView.as_view(), name="add_task"),
    path('update/<int:pk>', TaskUpdateView.as_view(), name="edit_task"),
    path('detail/<int:pk>', TaskDetailView.as_view(), name="detail_task"),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name="delete_task"),
    
]

