# Ex03_json_exam.py

'''
    data / sample.json 파일을 읽고 총합 구해서 출력
'''

f = open('./data/sample.json', 'r', encoding='utf-8')
data = f.read()
f.close()

import json
y = json.loads(data)

sum = 0
for k, v in y.items():
    sum += (v['price']*v['count'])

print('총합 : {0}원'.format(sum))