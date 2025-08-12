-- 頻出費目を効率よく検索するビューとインデックス
/*
CREATE TABLE 費目 (
ID     INTEGER PRIMARY KEY AUTOINCREMENT,
名前   VARCHAR(40) UNIQUE,
備考   VARCHAR(50) DEFAULT '不明' NOT NULL   
);

CREATE TABLE 家計簿 (
ID     INTEGER PRIMARY KEY AUTOINCREMENT,
日付   DATE NOT NULL,
費目ID INTEGER REFERENCES 費目(ID),
メモ   VARCHAR(100) DEFAULT '不明' NOT NULL,
入金額 INTEGER DEFAULT 0 CHECK(入金額 >= 0),
出金額 INTEGER DEFAULT 0 CHECK(出金額 >= 0)
); 

INSERT INTO 費目 (名前, 備考) 
VALUES 
('食費', '食料品・外食など'),
('交通費', '電車・バス・タクシー'),
('光熱費', '水道・電気・ガス'),
('医療費', '病院・薬'),
('教育費', '授業料・書籍'),
('娯楽費', '映画・ゲーム・旅行'),
('日用品', '生活消耗品')
ON CONFLICT(名前) DO UPDATE SET
備考 = excluded.備考;

INSERT INTO 家計簿 (日付, 費目ID, メモ, 入金額, 出金額)
VALUES
('2024-06-01', 1, 'スーパーで食材購入', 0, 4500),
('2024-06-02', 2, '電車で通勤', 0, 800),
('2024-06-03', 3, '水道代の支払い', 0, 3100),
('2024-06-04', 4, '病院で診察代', 0, 2200),
('2024-06-05', 5, '参考書購入', 0, 1800),
('2024-06-06', 6, '映画を観た', 0, 1500),
('2024-06-07', 7, 'トイレットペーパー購入', 0, 700),
('2024-06-08', 1, 'ランチ外食', 0, 1200),
('2024-06-09', 2, 'バス代（往復）', 0, 500),
('2024-06-10', 5, '受講料の支払い', 0, 10000);
*/
-- ① ビューの再作成
DROP VIEW IF EXISTS 費目別出金集計;

CREATE VIEW 費目別出金集計 AS
SELECT h.名前 AS 費目名, SUM(k.出金額) AS 合計
FROM 家計簿 k
JOIN 費目 h ON k.費目ID = h.ID
GROUP BY h.名前;

-- ② インデックスの作成
CREATE INDEX IF NOT EXISTS idx_家計簿_費目ID ON 家計簿(費目ID);

-- ※費目(ID)はPRIMARY KEYならインデックス済み

SELECT * FROM 費目別出金集計
ORDER BY 合計 DESC;