import jieba
import csv
title = [['キーワード']]
top_list=[]
content = jieba.cut("私はメールを送った。")
str_every_row = "←".join(content)
every_row = str_every_row.split("←")
for item in every_row:
    top_list.append([item])
with open(r'D:/jieba.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(title)
    writer.writerows(top_list)
