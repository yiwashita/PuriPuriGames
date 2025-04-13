#自作したソース
from django.urls import path
from . import views

urlpatterns = [
    path('', views.myprojectfunction), # トップページ
    path('recipe/', views.recipe), # レシピページ
    path('BrockDestroy/', views.BrockDestroy), # BrockDestroyページ

    path('unity/', views.unity_index),
]