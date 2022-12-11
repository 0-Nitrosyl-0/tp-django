from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.annuaire, name='annuaire'),
    path('info/',views.info, name='info'),
    
]