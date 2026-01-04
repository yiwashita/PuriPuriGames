"""
URL configuration for ppg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# URL とビュー（処理）を結びつける役割を持ちます。
# プロジェクトのurls.py    ：大まかな振り分け。このファイルで設定。
# アプリケーションのurls.py：詳細な URL 設定

urlpatterns = [
    path('admin/', admin.site.urls), # 管理サイトへのURL
    path('', include("ppgapp.urls")), # デフォルトアプリ、GSLB/～（アプリ側のurls.pyで設定）
    # path('practice/', include("ppgapp.urls")), # GSLB/practice/～（アプリ側のurls.pyで設定）
]
