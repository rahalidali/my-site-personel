from django.urls import path, include
from . import views

app_name='personaldetails'

urlpatterns = [
    path('', views.get_home),
    

]