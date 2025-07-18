### How to SQLAlchemy
#### venv 導入
```bash
$ python3 -m venv venv

# 有効化
$ source venv/bin/activate

# 無効化
$ deactivate
```

### PostgreSQLの導入
```bash
$ sudo apt update
$ sudo apt install postgresql postgresql-contrib
```

#### サービス起動：
```bash
$ sudo systemctl start postgresql
$ sudo systemctl enable postgresql
```

#### PostgreSQLにログイン：
```bash
$ sudo -u postgres psql
```

#### PostgreSQLシェル内でパスワード設定：
```bash
# ALTER USER postgres WITH PASSWORD 'your_password';
```

#### 終了：
```bash
# \q
```

#### 以降の接続：
```bash
$ psql -U postgres -h localhost -W
$ psql -U postgres -h localhost
```

### データベースの作成
```bash
# CREATE DATABASE mydb;
```

#### SQLAlchemy のインストール
```bash
$ pip install sqlalchemy
```

#### psycopg2 のインストール
```bash
$ pip install psycopg2-binary
$ pip install psycopg2
```

#### 基本的な流れ
- main.py と models.py を作成
- データベースにテーブルを作成する
- main.py 実行用
- models.py テーブルの形を定義する
- $ python main.py でテーブルが作成される
- VScode のPortgreSQL拡張機能で確認できる

#### dotenv をインポートする
- .envファイルを作成して個人情報を記載する
```t
DB_USER=postgres
DB_PASSWORD=
DB_HOST=localhost
DB_NAME=mydb
```
- dotenvをインストール
```bash
$ pip install python-dotenv
```

- dotenv をインポートする
```python
from dotenv import load_dotenv  # type: ignore
import os

def main():
    # .env ファイルを読み込む
    load_dotenv()

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")

    # 接続文字列を作成
    db_url = f"postgresql+psycopg2://{user}:{password}@{host}/{dbname}"

    engine = create_engine(
        db_url,
        echo=True,
    )

    # テーブル作成
    Base.metadata.create_all(engine)
```