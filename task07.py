prices = ["$120", "$340", "$50", "$90"]

def replace(text):
    return text.replace('$','')

result = map(replace,prices)
print(list(result))


# result = list(map(lambda x: x.replace('$', ''), prices))
# print(result)
