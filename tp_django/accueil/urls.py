from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.helloWorld, name='helloWorld'),
    #path('sum/<int:val1>/<int:val2>/',views.sum),
    re_path(r'sum/(?P<val1>\d+)/(?P<val2>\d+)/',views.sum),
]
