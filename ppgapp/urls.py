
# 自分で作ったファイル

from django.urls import path
from . import views

# プロジェクトのurls.py    ：大まかな振り分け
# アプリケーションのurls.py：詳細な URL 設定。このファイルで設定

urlpatterns = [
    path("hello/", views.hello_world, name="hello_world"),  # GSLB/hello/ でアクセス
    path("time/", views.current_time, name="current_time"),
    path("info/", views.show_request_info, name="request_info"),
    path("template/", views.hello_template, name="hello_template"),
    path("greeting/", views.greeting, name="greeting"),
    path("greet/<str:username>/", views.greet_user, name="greet_user"),

    path("", views.post_list, name="post_list"), # デフォルトサイト（トップページ）
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),  # 指定されたIDの記事を探すページ
]