sentence = "Functional programming in Python is very powerful and elegant"

words = sentence.split()

sorted_words = sorted(words, key=lambda x: len(x), reverse=True)

result = sorted_words[:3]

print(result)
