name = "sahithi"
print(name)
print('hey '+name)
age=20
country="india"
print(name,age,country)
print("my name is",name ,"i am",age ,"years old and iam from",country)
print("my name is %s i am %s years old and iam from %s"%(name,age,country))
marks = 86.68
print("my name is %s i am %s years old and i am from %s i got %s marks in my last sem"%(name,age,country,marks))
print("my name is {} i am {} years old and i am from {} i got {} marks in my last sem".format(name,age,country,marks))
print("my name is {3} i am {1} years old and i am from {0} i got {2} marks in my last sem".format(country,age,marks,name))
#f string
print(f"my name is {name} i am {age} years old and iam from {country}")
print(f"my name is {'sahithi'} i am {'20'} years old and iam from {'india'}")
print(f"2+2")
print(f"{2+2}")
print(f"{2-2}")
print(f"{2*2}")
print(f"{2/2}")
print(f"{2%2}")
print(f"my programming language is {'python'}")
print("""python zero to hero""")
#list
total_items = list()
total_items.append(70)
total_items.append(45.6)
total_items.append("sahithi")
total_items.append([3,4,5,6,7])
(total_items)
print(min([3,4,5,6,7]))
print(max([3,4,5,6,7]))
print(sum([3,4,5,6,7]))
print('for loop begins')
#for loop
for i in total_items:
    print(i)
for i in total_items:
    print(i,total_items.index(i))
for i in total_items:
    print(f'value is {i},index is {total_items.index(i)}')
print(len(total_items))
for i in range (len(total_items)):
    print(i)
for i in range (len(total_items)):
    print(f'value is {total_items[i]}, index is {i} ')
# tuple 
tuple_me = tuple()
print(type(tuple_me))
print(tuple_me.count(0))
tuple_me = (2,4,6,8,10,2,2,6,8,10)
print(tuple_me.count(2))
print(tuple_me.index(10))
print(len(tuple_me))
print(min(tuple_me))
print(max(tuple_me))
print(sum(tuple_me))
print(tuple_me)
#dict also known as JSON
print({
    'name':'sahithi',
    'age':20,
})
remember = dict()
print(type(remember))
remember['name']='sahithi'
print(remember)
remember['age']=20
print(remember)
remember['marks']=760
print(remember)
print(remember['name'])
remember['name']='sahithi-india'
print(remember['name'])
print(remember)
print(remember.keys())
print(remember.values())
print(remember.items())
for i,j in remember.items():
    print(i,j)
for i in remember.keys():
    print(i)
for j in remember.values():
    print(j)
for i in remember:
    print(i,remember[i])
for key in remember:
    print(key,remember[key])
for value in remember:
    print(value,remember[value])