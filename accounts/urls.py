from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns=[
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
