#自作したソース
from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.myprojectfunction),
]