from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_user/', views.add_user, name='add_user'),
    path('get_users/', views.get_users, name='get_users'),
    path('add_appointment_reminder/', views.add_appointment_reminder, name='add_appointment_reminder'),
    path('add_motivational_support/', views.add_motivational_support, name='add_motivational_support'),
]
