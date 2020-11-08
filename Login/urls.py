from django.contrib import admin
from django.urls import path
from Login import views
from Login.views import about
from Login.views import home
from Login.views import GeeksFormView
from Login.views import JS_Tutorial

urlpatterns = [
path('home',home.as_view()),

path('',about.as_view(),name='Home'),

path('parent',GeeksFormView.as_view(),name="parent"),

path('JS',JS_Tutorial.as_view(),name="JS")

]
