import re
from docx import Document

doc = Document('text.docx')
text = ''.join((p.text for p in doc.paragraphs))
result = re.findall(r'(([\u4e00-\u9fa5。、！：；，]).?\2)', text)

for word in result:
    print(word[0])