from django.urls import path
from . import views

urlpatterns = [
    path('', views.getting_started, name="getting_started"),
    path('signup/', views.signup, name="signup"),
    path('browse/', views.browse, name="browse"),
    path('home/', views.home, name="home"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('privacy_and_policy/', views.privacy_and_policy, name="privacy_and_policy"),
    path('term_of_use', views.term_of_use, name="term_of_use"),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('edit/<int:pk>/', views.edit_item, name="edit_item"),
    path('new/', views.new, name="new"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('delete/<int:pk>', views.delete_item, name="delete_item"),
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
    path('inbox/', views.inbox, name="inbox"),
    path('inbox/<int:pk>/', views.conversation_detail, name="conversation_detail"),

]