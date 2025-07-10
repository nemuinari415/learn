SELECT メモ, 出金額
  FROM 家計簿
 WHERE 出金額 > (
SELECT AVG(出金額) FROM 家計簿
)
 ORDER BY 出金額 DESC LIMIT 10;