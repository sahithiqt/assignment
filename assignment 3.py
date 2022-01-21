# user input
name = input("please enter your name :")
age = int(input("please enter your age :"))
country = input("where are you from :")
marks = float(input("how many marks did you get :"))
condition = bool(input("you passed the exam :"))
print(name,age,country,marks,condition)
print(type(name))
print(type(age))
print(type(country))
print(type(marks))
print(type(condition))

#for loop
totalinput = list()
for i in range(4):
    totalinput.append(input('please enter your hobbies : '))
print(totalinput)
for i in totalinput:
    print(i)
for i in totalinput:
    print(i,totalinput.index(i))
for i in range(len(totalinput)):
    print(i,totalinput[i])
print(*totalinput,sep ='-')
for i in totalinput:
    print(i,end= "--")

#if elif else (conditions)
for i in totalinput:
    if i.startswith('p'):
        print(f"\n{i} is very common hobby")
    elif i.startswith('r'):
        print(f"\n{i} is kind of intresting")
    elif i.startswith('s'):
        print(f"\n{i} nice....innovative hobby")
    else:
        print(f"\n{i} its intresting")
options = [2,'a',True,2.5,4,'s',False]
for i,j in enumerate(options):
    print(i,j, type(j))
for i,j in enumerate(options):
    if type(j)==int:
        print(f"this is an integer : {j}")
    elif type(j)==str:
        print(f"this is a string : {j}")
    elif type(j)==bool:
        print(f"this is a boolean : {j}")
    else:
        print(f"this is a float : {j}")

