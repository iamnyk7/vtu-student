from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('sgpa/<str:slug>',views.direct,name="direct"),
    path('calc',views.calc,name="calc"),
    path('cgpa',views.cgpa,name="cgpa"),
    path('cgpacalc',views.cgpacalc,name="cgpacal"),
]