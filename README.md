# PuriPuriGames

PuriPuriGames は、ゲームコンテンツを中心とした Web サイトです。  
Django を用いてバックエンドを構築し、静的ファイルおよび Unity WebGL コンテンツを配信します。

ローカル開発環境と本番（AWS EC2）環境で同一構成を維持することを前提としています。

---

## 概要

- Django による Web アプリケーション
- Gunicorn を用いた WSGI サーバ構成
- Nginx をリバースプロキシおよび静的ファイル配信として使用
- 将来的に HTTPS 対応予定

---

## 使用技術

| 種別 | 技術 |
|---|---|
| OS | Linux (Ubuntu) |
| 言語 | Python 3 |
| フレームワーク | Django |
| WSGI サーバ | Gunicorn |
| Web サーバ | Nginx |
| インフラ | AWS EC2 |
| バージョン管理 | Git |
