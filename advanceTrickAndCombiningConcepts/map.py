nums = [2,5,6,7,8,9,10]

#  map way 
def mapFunction(num) : 
    return num*2
nums = list(map(mapFunction,nums))
print(nums)


# comprehension way
nums = [num*2 for num in nums ]
print(nums)