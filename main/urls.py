from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_form, name='contact_form'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
]
