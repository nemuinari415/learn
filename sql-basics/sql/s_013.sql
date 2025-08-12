-- 各費目ごとに「出金額の合計」と「出金の平均」を求め、出金合計が 5,000 円を超える費目だけを多い順に表示
SELECT h.名前 AS 費目名,
       SUM(k.出金額) AS 出金合計,
       AVG(k.出金額) AS 出金平均
  FROM 家計簿 k
  JOIN 費目 h ON k.費目ID = h.ID
 GROUP BY 費目名
HAVING SUM(k.出金額) > 5000
 ORDER BY 出金平均 DESC;  