-- 顧客ごとに注文した商品の情報を一覧で表示
SELECT cd.customerid AS ID,
       cd.firstname || ' ' || cd.lastname AS 顧客名,
       od.orderitem AS 商品名,
       od.ordernum AS 注文数
  FROM 顧客データ cd
 INNER JOIN 注文データ od ON cd.customerid = od.customerid;