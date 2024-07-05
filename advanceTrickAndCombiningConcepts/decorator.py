def greet(fun) : 
    
    def wrapper(name) :
        #before
        print('hello')
        fun(name)
        # after 
        print('goodbye')
    
    return wrapper
@greet 
def sayName(name) :
    print(name)

sayName('khun thi han')