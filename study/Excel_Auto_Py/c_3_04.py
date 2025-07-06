import docx

doc = docx.Document("letter.docx")

# 段落を順次表示
for p in doc.paragraphs:
    print(p.text)