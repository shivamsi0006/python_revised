# list creation
'''l=[]
list_number=[1,2,3,4,5,6,7,8]
list_strings=["shivam","akash","rohit"]'''

# list can store the multiple items in single storage 

'''list=["shivam",24,45.5,True]
list1=[["shivam",1],["hello",2]]
'''
# list can assced by its indexing number. The index must be an integer.
'''
print(list[0]) 
    OUTPUT -> shivam
print(list1[0][0])
     OUTPUT -> shivam
# accesing the negative indexing 
print(list[-1])
    output ->  True'''

# getting the size of list 

'''print(len(list1))
    # output 2'''

#taking the input in list

'''list1=input("enter the number")
list1=list1.split()
print(list1)
# output 1 2 3 4 5 5'''

# adding elements in list by using the append method  (append method )
'''
list1=[]
list1.append(1)
list1.append('shivam')
list1.append((1,2))
print(list1)
'''

# adding an element at desired position  (insert method(indexing, value))

'''list1=[0]
list1.insert(2,1)
print(list1)
'''

# adding an element in list (Extend method) syntax- list.extend(iterable)
'''list1=[1,2,3,4]
list2=["h","e","l","l","o"]
list1.extend(list2)
print(list1)'''

# reversing a list using reverse method -> reverse()-return the sequence 

'''list1=[1,2,3,4,5,6]
list1.reverse()
print(list1)'''


# reversed function () reverse the list,tuple,string ,dictionary (its return the iterator object )

'''list1=[1,2,3,4,5]
list1=tuple(reversed(list1))
print(list1)'''

# removing an elements from list (remove method )- its only remove the single elements at a time 
# 2 condintion was elements should be present in a list

'''
list1=[1,2,3,3,4,5,6]
list1.remove(3)
print(list1)'''

# remove the elements from the list by using pop method (pop method ) in pop method we can pop elements by its index also 
'''list1=[1,3,2,4,"helo"]
list1.pop()
list1.pop(3)
print(list1)
'''
# more methods in lists 

# sort method ,count method ,index method 

'''l2=[("a",1),("b",0),("c",-1)]
l1=[1,2,3,4,5,6]
l2.sort(key=lambda x: x[1])
print(l2)'''

'''l1=[1,2,2,3,4,5,6]
c=l1.count(2)
print(c)'''

'''i=l1.index(2)
print(i)
'''

# list slicing 

'''list1=[2,3,4,5,6]
 #printing the list from starting to end poistion 
print(list1[:])

# printing the list from at a poistion to end 
print(list1[3:])

# print a list from starting poistion to definate poistion 
print(list1[:4])

# printing a list at step wise 
print(list1[::2])

# print a reversed list 
print(list1[::-1])
print(list1[-4:-1])'''


# (list comprehension) is used for creating the new list 
'''summ=0
list1=[str(x) for x in range(1,5)]
print(list1)'''