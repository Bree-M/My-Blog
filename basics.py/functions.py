#talk about enviromentalist, functions reuse 
#a function is a named block of code that does something when you call it
#defining a function
def say_hello():
    print("Hey, Pretty!")
say_hello()

#say_hello is calling the function and need to have paranthesis to be executed.
#functions can accept input called parameters

def greet(name):
    print(f"Hey {name}, you got this")

greet("Renee")    #calling the function, when using a function you always have to call it to print 
 
#returning values are used when you want to send a result back

def square(num):
    return num * num

result = square(5)
print(result)

# the difference between a function that prints and a function that returns is that returned values can be stored and used again.

# def function_name(parameter1, parameter2):
#     return something

#to use is as default
def greet(name="Renee"):
    print(f"Hey {name}, welcome back")

greet() #this is default
# greet("Renee")    

def make_coffee(type="black", sugar=True):
    if sugar:
        return f"Here's your sweet {type}"
    else:
        return f"Here's your bold {type}"
print(make_coffee("latte, True"))   

#functions are like giving names to your thoughts
#functions inside a function
def outer():
    def inner():
        print("Inner peace achieved")
    inner()
outer()    

#If variables are your words, functions are your sentences. They give your code rhythm, logic, and order. You’re not just coding now—you’re composing.