# python tuple can also store the multiple items at a time  and also different item same as list but there is difference between list and tuple is listt are mutable but tuple are immutable.

# collection of objects seprated by comma

# create a tuple
 
"""tupl1=("hello",1,2,3,4)"""

# create with single elements

'''tupl2=("hello",)
print(type(tupl2))
'''

# tuple constructor 
'''
tuple_constructor=tuple(("ds","hello","coding"))
print(tuple_constructor)
    # output  ('ds', 'hello', 'coding')'''

'''
str_tuple=tuple("hello")
print(str_tuple)
    # output ('h', 'e', 'l', 'l', 'o')
'''

# acessing the values in tuple
'''
t1=(1,2,3,4,5,6,7,"hello",)

# positive indexing 
print(t1[0])
# negative indexing 
print(t1[-1])'''


# different operation on tuple 

# concatenation of tuple 

'''t1=(1,2,3,4)
t2=("hello","devlopers")
t1=t1+t2
print(t1)'''

#nesting tuple 

'''t1=(1,2,3,4)
t2=("hello",)
print(type(t2))
t3=(t1,t2)
print(t3)'''

# Repetition tuple can create multiple items form a single elements 

'''t1=("hello",)*3
print(t1)'''

# slicing tuple slicing 
'''
t1=("hello",1,2,3,True,"devloper")
print(t1[0])
print(t1[-1])
print(t1[::-1])'''

# tuple method 

# count
'''t1=((2,3),3,[2,3],"3","hello")

print(t1.count((2,3)))
print(t1.count("3"))'''


# index method

"""print(t1.index((2,3)))

"""









