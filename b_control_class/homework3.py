

# 1
list_1 = [0, 3, 1, 7, 5, 0, 5, 8, 0, 4]
def quiz_2(list_data):
	a = set(list_data)
	return list(a)[1:5]

print(quiz_2(list_1))

# ➀ {1, 3, 4, 5}


# 2
def  delete_a_list_element(list_data, element_value):
	if element_value in list_data:
		list_data.remove(element_value)
		return list_data
	else:
		return "False"

list_data = ['a', 1, 'gachon', '2016.0']
element = float(2016)
result = delete_a_list_element(list_data, element)
print(result)

# ➃ False


# 3
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
def quiz_1(tuple_1, tuple_2):
	result = []
	for i in (tuple_1 + tuple_2):
		result.append(i)
	return result

print(quiz_1(tuple_1, tuple_2))

# ➀ [1, 2, 3, 4, 5, 6]


# [연습문제]

"""
- 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수 ( 함수명 : even_filter )
    [ 실행 ]
        print(even_filter([1, 2, 4, 5, 8, 9, 10]))

- 주어진 수가 소수인지 아닌지 판단하는 함수 ( 함수명 : is_prime_number )
    [ 실행 ]
        print(is_prime_number(60))
        print(is_prime_number(61))

- 주어진 문자열에서 모음의 개수를 출력하는 함수 ( 함수명 : count_vowel )
    [ 실행 ]
        print(count_vowel("pythonian"))
"""

# 1
def even_filter(ls):
    return [x for x in ls if x%2==0]

print(even_filter([1, 2, 4, 5, 8, 9, 10]))

# [2, 4, 8, 10]


# 3
def count_vowel2(word):
   vowel = ['a','e','i','o','u']
   cnt = 0
   for i in vowel:
      cnt += word.lower().count(i)
   return cnt

print(count_vowel2("pythonian"))
