# Ex02_csv.py

# csv 파일 -> 엑셀에서 열림 + 일반 에디터에서 열림
# Common String Value

data = [
    [1, '김', '책임'],
    [2, '박', '선임'],
    [3, '맹', '연구원']
]

import csv

# with open('./data/imsi.csv', 'w', encoding='utf-8') as f:
#     # f.write(data)
#     cout = csv.writer(f)
#     cout.writerows(data)

result = []
with open('./data/imsi.csv', 'r', encoding='utf-8') as f:
    cin = csv.reader(f)
    result = [row for row in cin if row]

print(result)