# global variable
name = 'khun thi han'

def sayMyName() : 
    # local 
    global name
    name = 'aung aung'
    print(name)

sayMyName();

print(name)