emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

def gmail(text):
    return text.endswith('gmail.com')

result = filter(gmail, emails)
print(list(result))
