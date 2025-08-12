-- 支出履歴を管理するテーブルを作成
CREATE TABLE 支出履歴 (
  ID     INTEGER PRIMARY KEY,
カテゴリ TEXT    DEFAULT '不明' NOT NULL,
金額     INTEGER  DEFAULT 0 CHECK(金額 >= 0),
メモ     VARCHAR(100) DEFAULT '不明' NOT NULL
)