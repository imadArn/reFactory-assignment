#Get input from user
start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

arr = []

if start < end:
    print ("Here is a list of leap years between " + str(start) + " and " + str(end)  + ":")

    while start < end:
        if (start % 4 == 0 and start % 100 != 0) or (start % 400 == 0):
            arr.append(start) 
        start += 1

elif start >= end:
    print("Check your year input again.")

length = len(arr)
# print(arr[length-1])
# print(length)
for i in arr:      
    if arr[length-1] == i:
        print(str(i)+'')
    else:
        print(str(i)+', ',end='')

