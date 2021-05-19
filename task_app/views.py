from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

#login view 
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

from django.urls import reverse_lazy
from .models import Task
from django import forms

class CustomLoginView(LoginView):
	template_name = "task_app/login.html"
	fields = '__all__'
	redirect_authenticated_user = True
 
class RegisterPage(FormView):
    template_name = 'task_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)
 
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
