
# 1

# [0, 1, 2, 0, 1]
a = [0, 1, 2, 3, 4]
print(a[:3], a[:-3])
# 결과 [0, 1, 2] [0, 1]


# 2

# [4, 3, 2, 1, 0]
a = [0, 1, 2, 3, 4]
print(a[::-1])
# print(a[::-2])    결과 : [4, 2, 0]


# 3

# egg salad bread lamb chicken apple
# egg salad bread lamb chicken
# [egg, salad, bread] [lamb, chicken] [apple]
first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
del john[2]
john.extend([order[2][0:1]])

print(john)


# 4

list_a = [3, 2, 1, 4]
list_b = list_a.sort()  # return 값이 없어서 b가 none
print(list_a, list_b)

list_b = sorted(list_a)
print(list_a, list_b)


# 5

# ['orange', 'strawberry', 'melon'] ['banana', 'orange']

fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])


# 6

num = [1, 2, 3, 4]
print(num * 2)


# 7

a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']
a.append('g')
b.append(6)
print('g' in b, len(b))


# 8

# (3)
# ['Hankook', 'is', 'academic', 'located', 'South Korea']
list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']
list_b = []
for i in range(len(list_a)):
    if i % 2 != 1:
        list_b.append(list_a[i])

print(list_b)


# 9

# admission_year = input("입학 연도를 입력하세요: ")
# print(type(admission_year))

# (3) str, str


# 10

# ["Korea", "Japan", "China", ["Seoul", [2, 3], "Beijing"]]

country = ["Korea", "Japan", "China"]
capital = ["Seoul", "Tokyo", "Beijing"]
index = [1, 2, 3]
country.append(capital)
country[3][1] = index[1:]
print(country)


# 11

# True
#


# =====================================================================


# 1

# 가 : stack
# 나 : queue
# 다 : tuple
# 라 : set


# 2

a = [3, "apple", 2016, 4]
b = a.pop(0)
c = a.pop(1)

print(b + c)        # (3 + 2016) = 2019

# a.pop(0) = [3]
# a.pop(1) = [2016]

# (1) 2019

# 3

# [1] = 2
# {, 1:2, 2:4, 3:6, 4:8, 6:10}
# dict_2[2] -> 4

dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}
dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())
dict_2 = dict()
for i in range(len(dict_keys)):
	dict_2[dict_values[i]] = dict_keys[i]

print(dict_2[2])


# 4

animal = ['cat', 'snake', 'monkey', 'ant', 'spider']
legs= [4, 0, 2, 4, 8]
animal_legs_dict = {}
for i in range(len(animal)):
	animal_legs_dict[legs[i]] = animal[i]
	animal_legs_dict['ant'] = 6

print(animal_legs_dict)

# (4)


# 5

# 2






# 7

data_1 = {'one' : (1,2,3,4,5,6), 'two' : [1,2,3,4,5,6], 'three' : {'four' : 4, 'five' : 5}}
for k in ['one','two','three']:
	try:
		print(data_1[k][:1])
	except TypeError:
		print("error")

for k in ['one', 'two','three']:
	try:
		data_1[k][-1] = "a"
		print(data_1[k][-1])
	except TypeError :
		print("error")

print(data_1['three'])