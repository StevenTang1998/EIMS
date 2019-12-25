from django.urls import path
from . import views


app_name = 'company'
urlpatterns = [
    path('search/<str:name>/'
         '<str:province>/<str:industry>/<str:capital>/<str:company_type>/<str:operating_status>/'
         '<int:page>/',
         views.search_company, name='search'),
    path('<int:pk>/', views.company_detail, name='detail'),
]
