/* 
カテゴリごとに最も出金額が高かった記録を1件ずつ表示してください。
結果には以下のカラムを含めてください：
- カテゴリ
- 出金額
- メモ
- 日付
出金額が同額で複数ある場合は、日付が新しい方を優先してください。
*/
SELECT カテゴリ, 出金額, メモ, 日付
FROM (
  SELECT h.名前 AS カテゴリ,
         k.出金額,
         k.メモ,
         k.日付,
         ROW_NUMBER() OVER (PARTITION BY h.名前 ORDER BY k.出金額 DESC, k.日付 DESC) AS rn
  FROM 家計簿 k
  JOIN 費目 h ON k.費目ID = h.ID
) AS sub
WHERE rn = 1
ORDER BY 出金額 DESC;
/*
| 部分                  | 意味                   |
| ------------------- | -------------------- |
| `ROW_NUMBER()`      | 行に連番をつける             |
| `PARTITION BY h.名前` | 費目ごとにグループ分けする        |
| `ORDER BY 出金額 DESC` | その中で金額の高い順に並べる       |
| `WHERE rn = 1`      | 各カテゴリで1番目（＝金額最大）のみ抽出 |
*/