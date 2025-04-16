#自作したソース
from django.urls import path
from . import views

urlpatterns = [
    path('', views.myprojectfunction), # トップページ
    path('recipe/', views.recipe), # レシピページ
    path('BlockDestroy/', views.unity_index), # BrockDestroyページ

]