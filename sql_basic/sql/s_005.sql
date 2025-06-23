-- 1回の注文で合計金額が3000円を超える注文だけを表示せよ
-- 条件付きフィルター（WHERE で金額計算）
SELECT cd.lastname || ' ' || cd.firstname AS 名前,
       od.orderitem AS 商品名,
       od.ordernum AS 注文数,
       cd.totalprice AS 合計金額
  FROM 注文データ od
  JOIN 顧客データ cd ON cd.customerid = od.customerid
 WHERE od.ordernum == 1 AND od.orderprice > 3000;