from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]