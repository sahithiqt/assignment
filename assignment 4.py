#functions

name = "sahithi"
age = 20
location = "india"
avg_marks = 80.0
marks = [70,80,90,85,75]
sub_marks = dict()
sub_marks['hindi'] = 70
sub_marks['english'] = 80
sub_marks['maths'] = 90
sub_marks['stats'] = 85
sub_marks['cs'] = 75
info = True
print(f"\nmy name is {name} \ni am {age} years old and i am from {location} \nmy average marks in last sem was {avg_marks} \nmarks in six subjects are {marks} \nmarks in each subject are {sub_marks} \nthe above information is {info}")
print(sub_marks.keys())
print(sub_marks.values())
print(sub_marks.items())
for i,j in sub_marks.items():
    print(i,j)
for i in sub_marks.keys():
    print(i)
for j in sub_marks.values():
    print(j)
for i in sub_marks:
    print(i,sub_marks[i])
for key in sub_marks:
    print(key,sub_marks[key])
for value in sub_marks:
    print(value,sub_marks[value])

def autobio(name,age,location,avg_marks,marks,info):
    print(f"\nmy name is {name} \ni am {age} years old and i am from {location} \nmy average marks in last sem was {avg_marks} \nmarks in six subjects are {marks} \n above information is {info}")
    print(type(autobio))
    autobio('sahithi',20,'india',80.0,[70,80,90,85,75],True)

    
def autobio(name,age,location,avg_marks,marks,info):
    return name,age,location,avg_marks,marks,info
print(autobio('sahithi',20,'india',80.0,[70,80,90,85,75],True))
ans = autobio('sahithi',20,'india',80.0,[70,80,90,85,75],True)
print(ans)
n , a, l, g, m, i = ans
print(n)
print(a)
print(l)
print(g)
print(m)
print(i)

def loop(l):
    for i in l:
        print(f"\nmy cal count today {i}")
loop([150,160,170,180,200])

def loop(l):
    print(f"\nmy total cal count {sum(l)}")
    print(f"\nmy least cal count is {min(l)}")
    print(f"\nno of days {len(l)}\n")
loop([150,160,170,180,200])

def loop(l):
    return sum(l)
print(loop([150,160,170,180,200]))
ans = loop([150,160,170,180,200])
print(ans)
ans = loop([150,160,170,180,200])
print(ans*2)
ans = loop([150,160,170,180,200])
print(ans+20)
ans = loop([150,160,170,180,200])
print(ans/2)
ans = loop([150,160,170,180,200])
print(ans-60)
ans = loop([150,160,170,180,200])
print(ans%5)

def loop(l):
    return min(l)
print(loop([150,160,170,180,200]))
ans = loop([150,160,170,180,200])
print(ans)
ans = loop([150,160,170,180,200])
print(ans*2)
ans = loop([150,160,170,180,200])
print(ans+20)
ans = loop([150,160,170,180,200])
print(ans/2)
ans = loop([150,160,170,180,200])
print(ans-60)
ans = loop([150,160,170,180,200])
print(ans%5)

def num(a):
    return a+2
numbers = [2,3,4,5,6,7,8,9,]
for a in numbers:
    print(f"\noriginal value was : {a}, added 2 to it : {num(a)}")
def num(b):
    return b+3
for b in numbers:
    print(f"\noriginal value was : {b}, added 3 to it : {num(b)}")

#while loop

a=5
while a<=15:
    print(a)
    a+=5

b=20
while b>=0:
    print(b)
    b-=5