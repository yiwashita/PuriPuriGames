#!/bin/bash

# 本番環境でのGunicornの起動スクリプト
# 停止する場合は「pkill gunicorn」を実行してくださいね

# Djangoプロジェクトのディレクトリに移動
if [ ! -d "/home/ubuntu/puripurigames" ]; then
    echo "Djangoプロジェクトのディレクトリが見つからないようです。。"
    exit 1
fi
cd /home/ubuntu/puripurigames

# Gunicornの起動
gunicorn puripurigames.wsgi:application \
  --bind unix:/home/ubuntu/puripurigames/puripurigames.sock \
  --workers 3 \
  --daemon

# 起動確認
if pgrep -f gunicorn > /dev/null; then
    echo "Gunicornが正常に起動し、ソケットファイルが作成されましたよ！"
    echo "変更を反映するには、Nginxをリロードしてくださいね"
else
    echo "あらら..Gunicornの起動に失敗しちゃいました"
    exit 1
fi
