# numbers = [4, -2, 0, 7, -9, 3, -1, 5]

# positive_numbers = list(filter(lambda x: x > 0, numbers))

# print(positive_numbers)




    #TODO filter() ishlashi

# text = "amjhbdfs,dfjgqu948593sjdfhg904"

# nums = filter(str.isdigit,text)
# print(list(nums))



# def is_lovel(s):
#     return s.lower() in ('a','u','o','i','e')

# text = "fkjvnqklejbgrlqnergjqkergrWAAAAUE"
# nums = filter(is_lovel,text)
# print(list(nums))



#TODO map() ishlashi

'''
def digit_to_word(d):
    if d == 1:
        return "bir"
    elif d == 2:
        return "ikki"

    elif d == 3:
        return "uch"

    elif d == 4:
        return "tort"
    
    elif d == 5:
        return "besh"
    
    elif d == 6:
        return "olti"

nums = [1,12,3,4,]
nums = map(digit_to_word,nums) # map() har biri ustida amal bajarish 
print(list(nums))'''


# def is_accepted(score):
#     return score >= 60

# scores = [77,65,77,88,97]

# result = all(map(is_accepted,scores))
# print(result)


#TODO lamda bu nomsiz funksiyacha 

scores = [60,64,345,66]

result = list(filter(lambda j: j >= 60,scores))
print(result)



























#TODO  murakkab funksiya

'''
from typing import Callable

def process(nums:list[int],func:Callable) -> list[int]:
    result = []

    for num in nums:
        result.append(func(num))

    return result

def power(a:int) -> int:
    return a ** 2

numbers = [3,4,7,4,2,4,6]
result = process(numbers,power)
print(result)

names = ["ali","vali"]
result = process(names,len)
print(result)

'''

#TODO murakkab funksiya

'''
# def process(data,func):
#     result = []

#     for item in data:
#         result.append(func(item))

#     return result

# def get_age(user):
#     return user['age']

# users = [

#     {"name":"ali","age":12},
#     {"name":"vali", "age":37}
# ]

# result = process(users,get_age)
# print(result)'''

