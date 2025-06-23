-- 出金額が20000円を超えるデータだけを、百円単位で四捨五入して表示
SELECT lastname || ' ' || firstname AS 名前,
       area AS 地区,
       age AS 年齢,
       totalprice AS 合計金額,
       ROUND(totalprice / 100.0) * 100 AS 百円単位の四捨五入 
FROM 顧客データ
WHERE totalprice > 20000;