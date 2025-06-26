nums = list(range(1, 21))

even_nums = filter(lambda x: x % 2 == 0, nums)

squares = map(lambda x: x**2, even_nums)

print(list(squares))

        

