#Count of even numbers using filter()
nums = [1, 2, 3, 4, 5, 6, 8]
result = len(list(filter(lambda x: x % 2 == 0, nums)))
print(result)