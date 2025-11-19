### AI Translation

**日本語** | [简体中文](README.md) | [English](README_en.md)

# 声明

0.本プロジェクトは商用利用を禁止します（使う人はいないと思いますが一応）。 1.智乃ブログのデザインインスピレーションとモチベーションは [KUN's Blog](https://soft.moe/) から来ていますが、コードは直接コピーしていません。すべて自分の感覚と少しの美的センスで AI にデザインさせました。 2.これは<font color="red">個人の理解 + AI</font>によるプロジェクトです。コードが乱雑なのはご容赦ください。2 日半で作った未完成品なので使い勝手は良くありません。 3.誰かが気に入るかもしれないのでオープンソースにしました。 4.何らかの理由で本プロジェクトが気に入らない場合は離れてください。気に入ったら STAR をお願いします。後半の説明に従って自由にデプロイして使えます。
5.Markdown ドキュメントを書くのは初めてなので分かりづらいかもしれません。

#

[![image](https://img.cdn1.vip/i/691d8b2dbfdd8_1763543853.webp)](https://github.com/Chino1116/chino_blog)

# <font color="#4671bb">智乃のブログ</font>

<center class="half">
<img src="https://img.cdn1.vip/i/691d8d539c502_1763544403.webp" width="580"/>
<img src="https://img.cdn1.vip/i/691d9a1a1785a_1763547674.webp" width="150"/>
</center>
<center class="half">
<img src="https://img.cdn1.vip/i/691d9b539fe20_1763547987.webp" width="150"/>
<img src="https://img.cdn1.vip/i/691d9b579106f_1763547991.webp" width="575"/>
</center>
<center class="half">
<img src="https://img.cdn1.vip/i/691d9b578c11e_1763547991.webp" width="580"/>
<img src="https://img.cdn1.vip/i/691d9b54177d7_1763547988.webp" width="150"/>
</center>

## 以下は雑談かもしれません

> Q:<font color="#4671bb">なぜこれを作ろうと思ったの？</font><br>A:他人のプログラムを使うのが好きじゃなくて、使いにくいし改造も面倒（実はコードが全然分からない）。<br><br>
> Q:<font color="#4671bb">作るきっかけは？</font><br>A:2023 年に最萌え Galgame サイトが誕生し、その後サイト管理人のブログ [KUN's Blog](https://soft.moe/) を見て、あまりにも自分好みだったので、2025 年 11 月 16 日に念願の.moe ドメインを購入。前置きは「ご注文はうさぎですか？」の香風智乃（かふう ちの）のローマ字（chino）に決定。こうして chino.moe が誕生し、その夜からブログ制作を開始。智乃のブログはこのような背景で生まれました。<br><br>
> Q:<font color="#4671bb">技術スタック NUXT + Flask + SQLite</font><br>A:フロントは NUXT4 を採用。フロント内容を固定したくなく SEO も考慮したため、技術力ゼロなので多数のフレームワークから NUXT を選択。コードだけ書けば OK。バックエンドは Python の Flask + SQLite で、設定や設計は面倒なので使い慣れたものを選択（できないから）。

### KUN's Blog スクリーンショット（神）

![image](https://img.cdn1.vip/i/691d8ce77f01f_1763544295.webp)

# <font color="#4671bb">デプロイ手順</font>

## フロントエンドのデプロイ

## 注意

<font color="red">フロント構築前に必ずバックエンド API を差し替えてください。</font>

### 前提条件

Node.js 20.x 以上がインストールされていること。

### 1.フロントエンド構築

ソースコードをローカルにダウンロードし、frontend フォルダに移動して以下のコマンドを実行し、.output フォルダを出力します。

```bash
npx nuxt build
```

### 2.フロントエンドをサーバーにデプロイ

.output フォルダをサーバーにアップロードし、以下のコマンドで起動。フロントはデフォルトで <font color="#4671bb">localhost:3000</font> で動作します。リバースプロキシでドメインを紐付けてください。

```bash
node .output/server/index.mjs
```

### 3.管理画面のアドレス

<font color="#4671bb">localhost:3000/chino</font> にアクセスして管理画面へ。ソースコードの pages/chino フォルダ名を変更すれば管理画面のアドレスも変わります。例: pages/admin にすれば <font color="#4671bb">localhost:3000/admin</font> になります。

## バックエンドのデプロイ

## 注意

バックエンド route/admin.py の下記コード位置で管理パスワードを変更してください。

```python
# 管理キー（環境変数や設定ファイルから取得推奨）
ADMIN_KEY = "Chino_Secret_1116"
```

### 前提条件

backend フォルダに入り、以下のコマンドで Python 依存ライブラリをインストール。

```bash
pip install -r requirements.txt
```

### バックエンドをサーバーにデプロイ

backend フォルダに入り、以下のコマンドで起動。バックエンドは <font color="#4671bb">localhost:8000</font> で動作します。リバースプロキシで API にドメインを紐付けてください。

以下のコマンドで起動。

```bash
python chino.py
```

または

```bash
python3 chino.py
```

### これでブログのデプロイは完了です

## ここまで読んだ方は本プロジェクトに興味があるはず。ぜひ無料の Star を！

### Star 推移

[![Star History Chart](https://api.star-history.com/svg?repos=Chino1116/chino_blog&type=date&legend=top-left)](https://www.star-history.com/#Chino1116/chino_blog&type=date&legend=top-left)
