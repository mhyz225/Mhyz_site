from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('resume/', views.resume, name="resume"),
    path('project/', views.project, name="project"),
    path('contact/', views.contact, name="contact")
]