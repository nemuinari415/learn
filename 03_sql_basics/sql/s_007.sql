-- 過去の注文データに存在しない**新規アイテム（未注文の商品）**をリストアップしてください。
SELECT item AS 商品名, itemprice AS 単価
FROM アイテムデータ
WHERE item NOT IN (SELECT orderitem FROM 注文データ)
ORDER BY itemprice DESC;