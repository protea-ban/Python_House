import re
from docx import Document
print("fdasfsad")
# 打开Word文件
doc = Document('test.docx')

# 遍历所有段的文本
for p in doc.paragraphs:
    # 获取每一段的文本
    t = p.text
    # 使用正则表达式提取章节信息
    m = re.match(r'第\d+章', t)
    if m:
        print(t)
    if '。(' in t:
        # 使用正则表达式提取题目编号
        num = re.match(r'\d+.\d+', t)
        print(num.group(0), end=' ')
        # 使用字符串方法和切片提取答案
        index = t.index('。（')
        print(t[index+2:t.rindex('）')])
