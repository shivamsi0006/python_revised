from functools import reduce

# A function is called a higher orer function in which we pass the function as parameter and in terms of return we get th function

'''def shout(text):
    return text.upper()
a=shout
print(a("text"))
'''

# passing a function to other function as an argument
'''
def upper(text):
    return text.upper()
def lower(text):
    return text.lower()
def greet(func):
    greeting =func("this is my text ")
    print(greeting)

greet(upper)
greet(lower)
'''

'''def create_adder(x):
    def adder(y):
        return x+y
    return adder
addx=create_adder(10)
print(addx(5))
'''

# lambda function

'''# swap of two nuber

x=lambda a,b:(b,a)
print(x(2,4))

# add two number

# x=lambda a,b:a+b
# print(x(2,4))

# checking even and odd number 
x=lambda a: "even" if a %2==0 else "odd"

print(x(3))
'''

# hof
# function return  sum of (even ,odd,number which is divisible by 3)
'''
def fun_sum(fun,l):
    result=0
    for i in l:
        if fun(i):
            result=result+i
    return result
l=[2,4,32,1,4,3,5,7,36,39,10]
even=lambda x: x%2==0
odd=lambda x: x%2!=0
number3=lambda x: x%3==0

print(fun_sum(even,l))
print (fun_sum(odd,l))
print(fun_sum(number3,l))'''

# map function takes function and iterable as arguments and return the map object - map function simply apply the operation on each memmber of iterable object 

# square of each number in list 

'''
l=[2,3,4,5,6,8,9,1]
new_list=list(map(lambda x :x**2,l))
print(new_list)

#  checking the list of number is even or odd 

new_list=(list(map(lambda x: 'even' if x%2==0 else "odd",l)))
print(new_list)

# fetch the number from list of dict

student =[{'name':"shivam","gender":"male","age":24},{'name':"akash","gender":"male","age":23}]

newlist=list(map(lambda x :x["name"],student))
print(newlist)'''

# filter function use to filter the iterables items filter the list
'''
l=[2,3,4,5,6,7,8]
new_list=list(filter(lambda x:x>4,l))
print(new_list)

# filter the fruits which are ending with e

l=["apple","grape","banana","gauva"]
new_list=list(filter(lambda x : x[-1]=='e',l))
print(new_list)
'''

# reduce function redduce the list size 
'''
l=[2,3,4,5,6,7,8,9]

# sum of list
new_list=reduce(lambda x,y:x+y,l)
print(new_list)


# find the greater number and smaller number 

greatest_number=reduce(lambda x,y: x if x>y else y,l)
print(greatest_number)

# find the lowest number 

lowest_number =reduce(lambda x,y:x if x<y else y ,l)
print(lowest_number)'''