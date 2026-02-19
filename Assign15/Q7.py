#Strings with length greater than 5 using filter()
words = ["python", "java", "programming", "code", "lambda"]
result = list(filter(lambda x: len(x) > 5, words))
print(result)
