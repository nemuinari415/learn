/*
「2024年6月に最も支出が多かったカテゴリ（費目名）とその合計出金額」を求めてください。
出力カラム：
- カテゴリ名
- 出金合計 
*/
SELECT h.名前 AS カテゴリ名,
       SUM(k.出金額) AS 合計出金額
  FROM 家計簿 k
  JOIN 費目 h ON k.費目ID = h.ID
 WHERE k.日付 BETWEEN '2024-06-01' AND '2024-06-30'
 GROUP BY h.名前
 ORDER BY 合計出金額 DESC
 LIMIT 1;