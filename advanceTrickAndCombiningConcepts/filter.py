nums = [1,2,3,4,5,6,7,8,9,10]


# for loop way
evenNumbers = []
for num in nums :
    if (num%2 == 0) :
        evenNumbers.append(num)

print('for loop even nums : ',evenNumbers)

# filter way
def even(num) : 
    return (num%2) == 0
    # if (num%2 == 0) : return True  
    # else :  return False

evenNums = filter(even,nums)
print('filter even nums : ',list(evenNums))

# comprehension
newNums = [num for num in nums if num%2 == 0 ]
print('newNums = ',newNums)

