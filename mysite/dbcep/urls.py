from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('reservation/',views.reservation,name='reservation'),
    path('menu/',views.menu,name='menu'),
    path('gallery/',views.gallery,name='gallery'),
    path('signup_user/',views.signup_user,name='signup_user'),
    path('signin_user/',views.signin_user,name='signin_user'),
    path('signout_user/',views.signout_user,name='signout_user'),
]