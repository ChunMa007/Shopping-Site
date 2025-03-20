from django.urls import path
from . import views

urlpatterns = [
    path('', views.getting_started, name="getting_started"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('privacy_and_policy/', views.privacy_and_policy, name="privacy_and_policy"),
    path('term_of_use', views.term_of_use, name="term_of_use"),
    path('detail/<int:pk>/', views.detail, name="detail"),
]