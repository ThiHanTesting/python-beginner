# with open('C:/Users/Khun Thi Han/Desktop/python/Beginning/advanceTrickAndCombiningConcepts/about.txt','w') as file : 
#     file.write('I am Khun Thi Han \n')

# # other work
# with open('C:/Users/Khun Thi Han/Desktop/python/Beginning/advanceTrickAndCombiningConcepts/about.txt','a') as file : 
#     file.write('\n I am 20 years old')

lists = ['I am Khun Thi Han ','\nI am 20 years old']

with open('C:/Users/Khun Thi Han/Desktop/python/Beginning/advanceTrickAndCombiningConcepts/about.txt','a') as file : 
    file.writelines(lists)