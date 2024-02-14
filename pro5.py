x= int(input("Enter a number of repetitions"))
# Write your decorator here
def repeat(func):
    def wrapper():
        for y in range(x):
            func()
    
    return wrapper
@repeat
def hello():
       print ('Hello')
hello()
