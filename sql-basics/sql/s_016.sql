/*
「2024年におけるカテゴリごとの月別出金合計」を集計してください。
以下の情報を出力してください：
- 月（例：2024-01）
- カテゴリ名（費目名）
- 月ごとの出金合計（そのカテゴリでの）
*/
SELECT strftime('%Y-%m', k.日付) AS 月,
       h.名前 AS カテゴリ,
       SUM(k.出金額) AS 出金合計
  FROM 家計簿 k
  JOIN 費目 h ON k.費目ID = h.ID
 WHERE k.日付 BETWEEN '2024-01-01' AND '2024-12-31' 
 GROUP BY 月, カテゴリ
 ORDER BY 月 ASC, カテゴリ ASC;