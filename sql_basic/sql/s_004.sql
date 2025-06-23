-- 全ての注文に対して、「顧客名」「商品名」「注文数」「注文金額」を表示せよ
SELECT cd.lastname || ' ' || cd.firstname AS 顧客名,
       od.orderitem AS 商品名,
       od.ordernum AS 注文数,
       od.orderprice AS 注文金額
  FROM 顧客データ cd
  JOIN 注文データ od ON od.customerid = cd.customerid
  JOIN アイテムデータ id ON id.item = od.orderitem;