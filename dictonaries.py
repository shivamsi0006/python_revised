
# dictonaries in python store the elements in key value pairs.


# update the key 1 

'''dict_items={
    "name":"hello",
    1:["coder","hello","programer"]
    ,2:56,

    1:56
}

print(dict_items)'''

# create an empty dictonaries and adding an elements 

'''d1={}
d1[1]=[1,2,3,4]
d1[2]=1,2,3,4
d1["values"]=23

print(d1)'''

# list of tuples 
'''
list_tuples=[("a",40),("b",20),("c",10),("d",0)]
d2=dict(list_tuples)
print(d2)
'''

# Accessing the dictionaries items by their key 
'''
d1={
    "name":"shivam",
    "age":24,
    "gender":"male"
    }
print(d1["name"])'''

# get method used to retrive the value of the key . if key is not present in the dict  then its return none as default 


'''d1={"name": "akash","detail":{"name":"akash","age":24,"gender":"male "}}

# its return not found 

print(d1.get("details"))

# nested dictonary access 

print(d1.get("detail").get("gender"))

# Acessing the dictonary without get method 

print(d1["detail"]['gender'])'''

# deleting a key in the dictonary 

'''
d1={"name": "akash","detail": "none"}

del(d1["detail"])

print(d1)'''

# mrthods apply in dictonary 

# clear method
'''
d1={"name": "aksh","age":"24","gender":"male"}
d1.clear()
print(d1)'''


# copy method  copy the dictonary

'''d2=d1.copy()
print(d2)

d2=d1
d2['name']="saini"
print(d1)
print(d2)
'''

#  fromkey method return the dictonary  take the the arguments key value and value to be optioanl 
'''
d1={}
key=("name","age","gender")

value=("None")
new_dict=d1.fromkeys(key)
print(new_dict)

values=("sahil",32,23)
new_dict=d1.fromkeys(key,values)
print(new_dict)

output={'name': ('sahil', 32, 23), 'age': ('sahil', 32, 23), 'gender': ('sahil', 32, 23)}'''

# d1.items returns a key value pair 
'''
d1={"name":"hello","work":'world'}
d2=d1.items()
print(list(d2)[0])'''

# d1.keys return the keys

'''d1={"name":"hello","work":'world'}
d2=d1.keys()
print(d2)
'''
# d1.pop the items by its key 
'''
d1={"name":"hello","work":'world'}
# d1.pop("name")

d1.pop("name","not_found")
print(d1)'''

# d1.popitem remove the elements from the last 
'''
d1={"name":"hello","work":'world'}
d2=d1.popitem()
print(d2)'''

# d1.setdefault return value of key if the key is not present it intsert it in the dict

'''d1={"name":"hello","work":'world'}
d2=d1.setdefault("new","akask")
print(d2)
'''
# d1.update the key if key is not present then its insert it 

'''d1.update({"name":"shivam"})
print(d1)'''

# d1.values returns the value object

''' 
d1={"name":"akash",'gender':"male",'age':24}
d2=d1.values()
print(d2)'''