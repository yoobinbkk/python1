

# [제어문 2]

# 1
mylist = ['apple' ,'banana', 'grape']
result = list(enumerate(mylist))
print(result)

# ➂ [(0, 'apple'), (1, 'banana'), (2, 'grape')]


# 2
cat_song = "my cat has blue eyes, my cat is cute"
print({i:j for j,i in enumerate(cat_song.split())})

# ➃ {'my': 5, 'cat': 6, 'has': 2, 'blue': 3, 'eyes,': 4, 'is': 7, 'cute': 8}


# 3
colors = ['orange', 'pink', 'brown', 'black', 'white']
result = '&'.join(colors)
print(result)

# 'orange&pink&brown&black&white'


# 4
user_dict = {}
user_list = ["students","superuser", "professor", "employee"]
for value_1, value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
print(user_dict)

# {'students': 0, 'superuser': 1, 'professor': 2, 'employee': 3}


# 6
animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl']
print([ani for ani in animal if 'o' not in ani])

# ['Cat', 'Panda', 'Owl']


# 7
name = "Hanbit University"
student = ["Hong", "Gil", "Dong"]
split_name = name.split()
join_student = ''.join(student)
print(join_student[-4:] + split_name[1])

# DongUniversity


# 8
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2' ,'b3']
for a, b in zip(alist, blist):
    print(a, b)
"""
a1 b1
a2 b2
a3 b3
"""


# 9
a = [1, 2, 3]
b = [4, 5, ]
c = [7, 8, 9]
print([[sum(k), len(k)] for k in zip(a, b, c)])

# ② [[12, 3], [15, 3]]


# 10
week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
list_data = [week, rainbow]
print(list_data[1][2])

# yellow


# 11
kor_score = [30, 79, 20, 100, 80]
math_score = [43, 59, 0, 30, 90]
eng_score = [49, 72, 48, 67, 15]
midterm_score = [kor_score, math_score, eng_score]
print ("score:",midterm_score[2][1])

# 72


# 12
alist = ["a", "b", "c"]
blist = ["1", "2", "3"]
abcd= []
for a, b in enumerate(zip(alist, blist)):
    try:
        abcd.append(b[a])
    except IndexError:
        abcd.append("error")

print(abcd)


# 13
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0]
print(len(answer))

# 80



