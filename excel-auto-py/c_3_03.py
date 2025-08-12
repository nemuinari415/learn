# python-docx を使うのに必要な宣言
import docx

# 新規ドキュメントを作成
doc = docx.Document()

# 既存Wordファイルを読み込み
doc = docx.Document('ファイル名.docx')

# Wordファイルへ保存
doc.save('ファイル名.docx')