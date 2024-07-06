# file=open('C:/Users/Khun Thi Han/Desktop/python/Beginning/advanceTrickAndCombiningConcepts/text.txt')

# # for line in file : 
# #     print(line)

# # lineLists = file.readlines()
# # print(lineLists)

# file.seek(50)
# paragraph = file.read(100)
# print(paragraph)

# file.close()



with open('C:/Users/Khun Thi Han/Desktop/python/Beginning/advanceTrickAndCombiningConcepts/text.txt') as file :
    paragraph = file.read(100)
    print(paragraph)