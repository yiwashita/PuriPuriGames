from django.shortcuts import render
from django.http import HttpResponse # レスポンスを返すためのクラスをインポート
from datetime import datetime

# Create your views here.
# URL に対する処理を記述

def hello_world(request):
    return HttpResponse("Hello Django!")

def current_time(request):
    now = datetime.now()
    html = f"<html><body>現在時刻は {now} です。</body></html>"
    return HttpResponse(html)

def show_request_info(request):
    info = f"""
    <html>
    <body>
        <h1>リクエスト情報</h1>
        <p>メソッド: {request.method}</p>
        <p>パス: {request.path}</p>
        <p>ユーザーエージェント: {request.META.get('HTTP_USER_AGENT', 'なし')}</p>
    </body>
    </html>
    """
    return HttpResponse(info)

def hello_template(request):
    return render(request, "ppgapp/hello_template.html")

def greeting(request):
    context = {
        "name": "めんご",
        "age": 25,
        "hobbies": ["プログラミング", "読書", "散歩"],
        "user": {"name": "太郎", "email": "taro@example.com"},
        "is_logged_in": True,
    }
    return render(request, "ppgapp/greeting.html", context)

def greet_user(request, username):
    context = {
        "username": username,
    }
    return render(request, "ppgapp/greet_user.html", context)



# 仮の共通記事データ（後でデータベースから取得するようになります）
POSTS = [
    {
        "id": 1,
        "title": "Djangoを始めました",
        "content": "Djangoの学習を始めました。楽しいです！",
        "created_at": "2026-01-03",
        "body": """今日からDjangoの学習を始めました。
Pythonは少し触ったことがあったけど、Webフレームワークは初めてです。
最初は難しそうだと思ったけど、チュートリアルが分かりやすくて助かります。
これからブログアプリを作っていきたいと思います！""",
    },
    {
        "id": 2,
        "title": "ビューについて学んだこと",
        "content": "今日はビューについて学びました。",
        "created_at": "2026-01-03",
        "body": """Djangoのビューは、リクエストを受け取ってレスポンスを返す関数です。
MVTパターンのVに当たる部分で、ビジネスロジックを担当します。
テンプレートにデータを渡す方法も学びました。
contextという辞書を使うのが面白いです。""",
    },
    {
        "id": 3,
        "title": "テンプレートは便利",
        "content": "テンプレートを使うとHTMLが書きやすいです。",
        "created_at": "2026-01-03",
        "body": """今日はテンプレートについて学習しました。
変数の表示、forループ、if文など、基本的な機能を試しました。
特に継承システムが素晴らしいです！
共通部分を一箇所にまとめられるのは、とても効率的ですね。""",
    },
]

def post_list(request):
    context = {
        "posts": POSTS,
    }
    return render(request, "ppgapp/post_list.html", context)

def post_detail(request, post_id):
    # 指定されたIDの記事を探す
    post = None
    for p in POSTS:
        if p["id"] == post_id:
            post = p
            break

    context = {
        "post": post,
        'posts': POSTS,  # サイドバー用に追加
    }
    return render(request, "ppgapp/post_detail.html", context)