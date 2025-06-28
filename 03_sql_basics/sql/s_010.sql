-- 人気商品のランキングを表示
SELECT orderitem AS 商品名, SUM(ordernum) AS 合計注文数
  FROM 注文データ
 GROUP BY orderitem
 ORDER BY 合計注文数 DESC LIMIT 3;