"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None


a = -1

if a:
    print('True')
else:
    print('False')

b = 0
z = 2

if a and b:
    print('True2')  # True, b=0이면 False

if a or b:
    print('True3')  # True

print(a and b)      # and는 둘 다 확인하고 뒷자리의 값을 출력한다. 만약 이중에 0이 있다면 0을 출력한다.
print(b or z)       # or는 첫 값이 True면 그 값을 출력한다. 만약 첫 값이 False고 두번 째 값이 True면 True인 값을 출력한다. 만약 둘 다 False면 0을 출력한다.

# print(b or c or a)

if a:
    c = 2
elif b:
    c = 4
else:
    c = 6

print(c)

# 파이썬에서는 지역변수, 전역변수 구분이 없는 것 같다.
# if문의 변수값도 바깥에서 잘 적용된다.
