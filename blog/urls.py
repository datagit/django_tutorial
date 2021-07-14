from django.urls import path
from . import views

urlpatterns = [
  path('', views.list, name = 'blog'),
  path('<int:id>/', views.detail, name = 'post'),
]