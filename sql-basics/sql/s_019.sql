/*「2024年に記録された支出（出金額）のうち、カテゴリ別に月平均出金額が最も多いカテゴリ名とその金額を求めよ」*/
with 月合計出金額 AS (
    SELECT strftime('%Y-%m', K.日付) AS 月,
           H.名前 AS カテゴリ,
           AVG(K.出金額) AS 平均出金額
      FROM 家計簿 K
      JOIN 費目 H ON K.費目ID = H.ID
     WHERE K.日付 BETWEEN '2024-01-01' AND '2024-12-31'
     GROUP BY カテゴリ, 月
)
SELECT カテゴリ, 平均出金額
  FROM 月合計出金額
 ORDER BY 平均出金額 DESC LIMIT 1;

 /*
 WITH 月別カテゴリ出金 AS (
    SELECT
        strftime('%Y-%m', K.日付) AS 月,
        H.名前 AS カテゴリ,
        SUM(K.出金額) AS 月出金合計
    FROM 家計簿 K
    JOIN 費目 H ON K.費目ID = H.ID
    WHERE K.日付 BETWEEN '2024-01-01' AND '2024-12-31'
    GROUP BY 月, カテゴリ
),
カテゴリ別月平均 AS (
    SELECT
        カテゴリ,
        AVG(月出金合計) AS 月平均出金額
    FROM 月別カテゴリ出金
    GROUP BY カテゴリ
)
SELECT
    カテゴリ,
    月平均出金額
FROM カテゴリ別月平均
ORDER BY 月平均出金額 DESC
LIMIT 1;
*/