from django.urls import path
from authors import views

appname = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='register'),
]
