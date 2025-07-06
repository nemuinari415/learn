html_str = "<html<body>...(/body)(/html)"

# import でライブラリの取り込み
from bs4 import BeautifulSoup
# BeautifulSoup で解析を行う
soup = BeautifulSoup(html_str, "html5lib")

# 内容を出力
print(soup.prettify())