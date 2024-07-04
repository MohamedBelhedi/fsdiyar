from fahrschulemanager_fullstack import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='loginregister'),
    path('home/', views.home, name='home'),
    path('pruefungen/', views.pruefung, name='pruefung'),

]
