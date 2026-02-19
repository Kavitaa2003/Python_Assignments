#Minimum element using reduce()
from functools import reduce

nums = [10, 25, 3, 40, 15]
result = reduce(lambda a, b: a if a < b else b, nums)
print(result)