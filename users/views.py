from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from users.forms import LoginForm, RegisterForm
from .serializer import UserSerializer
from .models import User

from rest_framework.views import APIView



def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

class LoginView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    extra_context = {'title': 'Authentication'}

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.data)
        if form.is_valid():
            username = request.data['username']
            password = request.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
        else:
            return render(request, 'users/login.html', {'form': form})

def exception(request):
    return render(request, 'users/exception.html')
class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            # Redirect to the registration done page
            return redirect(reverse('users:registration_done'))
        else:
            form = RegisterForm(request.POST)
            return render(request, 'users/register.html', {'form': form})

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.data.get('password'))
        user.save()

def registration_done(request):
    return render(request, 'users/register_done.html')

