from django.urls import path
from . import views


app_name = 'human'
urlpatterns = [
    path('<str:name>/', views.human, name='detail'),
]
