#lambda
x = lambda a : a + 2
print(x(5))
y = lambda b : b - 5
print(y(10))
list = lambda l : sum(l)
print(list([3,5,7,9,2,]))

#list comprehension
print([f"set - {i}" for i in [1,2,3,4,5,6,7,8,9]])
print([f"{j} is multiple of 3" for j in [2,3,4,5,6,7,8,9] if j%3==0])
print([f"{k} is multiple of 5" if k%5==0 else f"{k} is not a multiple of 5" for k in [2,4,5,7,10,13,15,17,18,20]])
print([f"{m*2} is multiple of 4" for m in [2,4,6,8,10,12,14,16,18,20]])