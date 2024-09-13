from django.urls import path
from . import views
from .views import toggle_task

urlpatterns = [
  path('', views.home, name='home'),
  path('toggle-task', toggle_task, name='toggle_task'),
  path('create-task', views.create_task, name='create_task'),
]