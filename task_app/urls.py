from django.urls import path
from .views import CustomLoginView, TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView
from django.contrib.auth.views import LogoutView

#This is where we add all the urls for our applications
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("", TaskList.as_view() , name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view() , name="detail-task"),
    path("create-task/", TaskCreate.as_view() , name="create-task"),
    path("update-task/<int:pk>/", TaskUpdate.as_view() , name="update-task"),
    path("delete-task/<int:pk>/", DeleteView.as_view() , name="delete-task"),
    path("logout/", LogoutView.as_view(next_page = 'login'), name="logout"),
]
