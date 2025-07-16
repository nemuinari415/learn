-- ステップ①：カテゴリ・月ごとの出金合計を出す
WITH 月別カテゴリ集計 AS (
  SELECT 
    h.名前 AS カテゴリ名,
    strftime('%Y-%m', k.日付) AS 月,
    SUM(k.出金額) AS 月出金合計
  FROM 家計簿 k
  JOIN 費目 h ON k.費目ID = h.ID
  WHERE k.日付 BETWEEN '2024-01-01' AND '2024-12-31'
  GROUP BY カテゴリ名, 月
)

-- ステップ②：カテゴリごとの出金合計・月数・月平均を出す
SELECT 
  カテゴリ名,
  SUM(月出金合計) AS 出金合計,
  COUNT(月) AS 月数,
  ROUND(AVG(月出金合計)) AS 月平均出金額
FROM 月別カテゴリ集計
GROUP BY カテゴリ名
ORDER BY 出金合計 DESC;
