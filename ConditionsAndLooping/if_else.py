# age = int(input('age : '))

# if age < 18 : 
#     print('you are yound')
# elif age>18 and age<30 : 
#     print('you are adult')
# else : 
#     print('you are old')

# tired = input(' r u tired "y/n"') 

# if tired == 'y' : print('rest well')
# elif tired == 'n' : print('go back to work')
# else : print('only y or n plz ')

username = 'Khun Thi Han'
password = '123456'

inputUsername = input('username : ')
inputPassword = input('password : ')

if(username != inputUsername  ) : print('user doesn\'t exit')
elif(password != inputPassword ): print('password wrong')
else : print(f'welcome back {inputUsername}') 

