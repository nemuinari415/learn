### Flask チュートリアル

#### Flask のインストール
```bash
# bash
pip install Flask
```

#### 最初のアプリを作成
```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

#### アプリ起動
```bash
# bash
python app.py
```

#### ルーティングの追加
URLごとに関数を申し込める。
```python
@app.route("/user/<username>")
def show_user(username):
    return f"ユーザー名: {username}"
```

### テンプレートの利用(HTMLファイル)
ディレクトリ：templates/index.html
```html
<!-- index.html -->
<!doctype html>
<title>Hello from Flask</title>
<h1>{{ message }}</h1>
```
```python
# app.py
from flask import render_template

@app.route("/greet/<name>")
def greet(name):
    return render_template("index.html", message=f"こんにちは、{name}さん！")
```
```text
解説：
render_template は HTML テンプレートファイル（例: index.html）を読み込んで、ブラウザに表示するための関数です。

@app.route("/greet/<name>") とは？
@app.route(...) は Flask に「このURLにアクセスされたとき、どの関数を呼び出すか」を教える"ルーティング（経路定義）"です。

/greet/<name> は 動的ルートです。

動的ルートとは？
/greet/<name> の <name> の部分は変数として扱われます。

たとえば以下のようにURLを入力すると：
```
```bash
http://localhost:5000/greet/レオン
```
```text
Flaskは greet("レオン") のように、自動で "レオン" を name に代入してくれます。

def greet(name):
上記のように、URLで渡された name の値が引数として関数に入ってきます。

return render_template("index.html", message=...)
index.html というテンプレートファイルを使ってHTMLを生成します。

ここで message という名前の変数に、文字列 こんにちは、◯◯さん！ を代入して渡しています。

HTMLテンプレート内で {{ message }} のように使うことで、表示されます。
```


#### フォームの受け取り
HTMLフォームから値を受け取る。
```python
# app.py
from flask import request

@app.route("/post", methods=["POST"])
def post():
    data = request.form["data"]
    return f"送信されたデータ: {data}"
```
#### 具体的な使い方
```html
<body>
    <form action="/greet" method="post">
        <label>名前：</label>
        <input type="text" name="name">
        <button type="submit">送信</button>
  </form>
</body>
```
```python
from flask import request

@app.route("/greet", methods=["POST"])
def greet_post():
    name = request.form["name"]
    return render_template("index.html", message=f"こんにちは、{name}さん！")
```
#### GETにしたい場合
```html
<form action="/greet" method="get">
    <input type="text" name="name">
```
```python
@app.route("/greet")
def greet():
    name = request.args.get("name")
    return render_template("index.html", message=f"こんにちは、{name}さん！")
```
```text
request.args.get("name") → GETパラメータ（クエリ文字列）を受け取る
```
```text
postgreSQL, flask_sqlalchemy, SQLAlchemy
```