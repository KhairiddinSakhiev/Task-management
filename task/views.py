from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = "tasks_list.html"

class TasksCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "create.html"
    
    success_url = reverse_lazy("task_list")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class TaskUpdateView(UpdateView):
    model = Task
    template_name = "update.html"
    fields = ['title', 'user', 'due_date', 'is_done']
    success_url = reverse_lazy("task_list")
    
class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")
    




