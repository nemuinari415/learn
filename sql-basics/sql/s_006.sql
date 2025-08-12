-- 各社員が担当した注文の「合計金額」と金額が 10000円を超える社員だけを表示
SELECT firstname || ' ' || lastname AS 顧客名,
       age AS 年齢,
       SUM(totalprice) AS 合計金額
  FROM 顧客データ
 GROUP BY 顧客名 HAVING 合計金額 > 10000
 ORDER BY 合計金額 DESC;