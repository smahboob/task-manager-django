from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#login view 
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from .models import Task


class CustomLoginView(LoginView):
	template_name = "task_app/login.html"
	fields = '__all__'
	redirect_authenticated_user = False
 
class TaskList(ListView):
	model = Task
	context_object_name = 'task_list'
 
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task_detail'
    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class DeleteView(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy('tasks')
