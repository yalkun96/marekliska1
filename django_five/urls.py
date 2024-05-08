from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('addnote', AddNoteView.as_view(), name='addarticle'),
    path('contact/', contact, name='contact'),
    path('edit/<slug:slug>/', edit, name='edit'),
    path('delete/<slug:slug>/', delete_post, name='delete_post'),
    path('leave_comment/', leave_comment, name='leave_comment'),
    path('article/<slug:slug>/', article, name='article')
]
