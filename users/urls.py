from django.urls import path

from .views import *


app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('regitration_done/', registration_done, name='registration_done'),
    path('register/api/', Register.as_view(), name='register'),
    ]