from django.urls import path
from . import views


app_name = 'human'
urlpatterns = [
    path('search/<str:name>/<str:position>/<int:page>/', views.search_human, name='search'),
    path('<str:name>/', views.human, name='detail'),
]
