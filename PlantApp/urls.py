from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home),
    path('pred',views.home,name='home')
]
