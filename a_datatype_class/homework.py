import math
import numpy as np

# 1
# a = int(input('정수를입력하세요: '))
# b = int(input('정수를입력하세요: '))
# c = int(input('정수를입력하세요: '))
# d = int(input('정수를입력하세요: '))
# e = int(input('정수를입력하세요: '))
#
# print('평균 =', (a+b+c+d+e)/5)


# 2
# result = input('문자열을 입력하세요>>')
# print(result[::-1])



# 3

# *************************************************************
# sum = 0
# list = [int(i) for i in input('입력>>>').split()]
# print('평균 : {0}, 표준편차 : {1}'.format(np.mean(list), np.std(list)))
# *************************************************************


# numbers = input('정수리스트입력:')     #입력값 받아오기
# nums = numbers.split()              #list로 변환
# sum = 0.0                           #총합변수 선언
# for i in range(len(nums)):          #총합 계산
#     sum += float(nums[i])
#
# avg=sum/len(nums)                   #평균수 계산
#
# # 표준편차계산(수학문제)
# aa = 0.0
# for i in range(len(nums)):
#     aa += abs(float(nums[i])-avg)**2
# bb = aa/(len(nums)-1)
# bb=math.sqrt(bb)
#
# print('평균= {}'.format(avg))
# print('표준편차{:.2f}'.format(bb))


# 4

l = list(input('문자 입력>>>'))

alphabet = "ABC DEF GHI JKL MNO PQRS TUV WXYZ"
alp = alphabet.split()

print(l)
print(alp)

ans = ""
for x in range(len(l)):
    for i in range(len(alp)):
        ans += alp[i].find(l[x])

print(ans)

# phonenum =[[],['A','B','C'],['D','E','F'], ['G','H','I'],['J','K','L'],['M','N','O'],
#            ['P','Q','R','S'],['T','U','V'], ['W','X','Y','Z']]
# output = input('문자열을입력하시오: ')
# result = ''
# for num in output:
#     for i in range(len(phonenum)):
#         if num.upper() in phonenum[i]:
#             # 1에는 아무 문자가 없기 때문에 1을 더해준다
#             # 숫자값끼리 더하면 합한 값이 나오기 때문에 str로 형 변환
#             result += str(i+1)
# print(result)