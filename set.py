# set is an unorderd collection type mutable ,no duplicate items 
# because no duplicate items thats why set are unorder collections

'''set_elements={1,"hello",True,5.2}
print(type(set_elements))
'''

# frozen set define we can not modify the frozen set make it immutable 

'''set1={1,2,3,4,"hello"}
set2=frozenset({1,1,3,4,"hello"})
print(type(set1))
set1.add(20)
print(type(set2))'''

# methods of set 

set1={1,2,3,3,4,"hello","coder"}
set2={1,2,"hello"}
set3={2,"hello","c"}

# add method 

'''set1.add(0)
print(set1)'''

# remove method

'''set1.remove("hello")
print(set1)'''

# update method use when we want to add another iterable set 
'''
set1.update({20,30,40})
print(set1)'''

# set1.difference method  return a new set which is present in this set but not in the other set 

'''new_set=set1.difference(set2)
print(new_set)
'''
# set1.discard method -remove the elements from the set if its presents 

'''print(set1.discard(2))
print(set1)'''

# set1.intersection common in both the sets

'''new_set=set1.intersection(set2)
print(new_set)
'''
# set1.difference_update same as difference but it does not return a new set its update in the same set 
'''
set1.difference_update(set2)
print(set1)

# output - {3, 4, 'coder'}'''

# set1.intersection_update its also update in the same set 

'''set1.intersection_update(set2)
print(set1)
'''
# set1.issubset return true or false 

'''print(set2.issubset(set2))
'''
# set1.union return union of set 

'''new_set=set1.union(set3)
print(new_set)'''