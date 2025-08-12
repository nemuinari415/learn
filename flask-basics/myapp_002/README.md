# myapp_002
英単語帳アプリ
※1日1語1句を記録して、ランダム表示させる機能

## DataBase : english.db
### Table : words

| id  | word     | meaning      | example_sentence      | translation         |
|-----|----------|--------------|-----------------------|---------------------|
| 1   | apple    | a fruit      | I ate an apple.       | 私はりんごを食べた。|
| 2   | run      | to move fast | He runs every day.    | 彼は毎日走る。      |

### Column Definitions

| Column Name         | Type    | 日本語訳     | 備考                             |
|---------------------|---------|--------------|----------------------------------|
| id                  | INTEGER | 識別番号     | ユニークな番号（自動付与）       |
| word                | TEXT    | 英単語       | 覚えたい単語                     |
| meaning             | TEXT    | 意味（英語） | 英語での簡潔な定義               |
| example_sentence    | TEXT    | 例文（英語） | 使い方の文                       |
| translation         | TEXT    | 和訳         | 例文の日本語訳                   |

---
### Table : users

| user_id | user_name | email | password_hash | start_date |
|---------|-----------|-------|---------------|------------|
|         |           |       |               |            |

### Column Definitions

| Column Name   | Type     | Description                 |
|---------------|----------|-----------------------------|
| user_id       | INTEGER  | ユーザーID（主キー）        |
| user_name     | TEXT     | ユーザー名                  |
| email         | TEXT     | メールアドレス（任意）      |
| password_hash | TEXT     | パスワード（ハッシュ化）    |
| start_date    | DATE     | 学習開始日（〇日目表示用）  |


## Planning Design