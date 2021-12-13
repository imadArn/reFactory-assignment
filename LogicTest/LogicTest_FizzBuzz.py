inp = input("input :")
arr=[]

for i in range(1,int(inp),1): #(start,stop,step)
    if i % 3 == 0 and i % 5 == 0:
        arr.append("FizzBuzz")
        continue
    elif i % 3 == 0:
        arr.append("Fizz")
        continue
    elif i % 5 == 0:
        arr.append('Buzz')
        continue
    arr.append(i)
print(arr)
