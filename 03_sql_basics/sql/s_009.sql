-- 在庫不足を検出する
SELECT od.orderitem AS 商品名,
       sd.stock AS 在庫数,
       od.ordernum AS 注文数, 
       od.ordernum - sd.stock AS 超過数
  FROM 注文データ od
  JOIN 在庫データ sd ON od.orderitem = sd.item
 WHERE od.ordernum > sd.stock
 ORDER BY 超過数 DESC;