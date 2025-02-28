from django.urls import path
from hello_api import views

urlpatterns = [
    path('api/hello/', views.hello_world, name='hello_world'),
]