arr = []

# number of elements as input
# hit the enter keys after entring the number one by one 
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    arr.append(ele) 

num = sum(arr)

def toFindNearestFibonacci(num):
     
    # Base Case
    if (num == 0):
        print(0)
        return
 
    # Initialize the first & second
    # terms of the Fibonacci series
    first = 0
    second = 1
 
    # Store the third term
    third = first + second
 
    # Iterate until the third term
    # is less than or equal to num
    while (third <= num):
         
        # Update the first
        first = second
 
        # Update the second
        second = third
 
        # Update the third
        third = first + second
 
    # Store the Fibonacci number
    # having smaller difference with N
    if (abs(third - num) >=
        abs(second - num)):
        ans =  second
    else:
        ans = third
 
    # Print the result = ans-sum(input)
    print(ans-num)

toFindNearestFibonacci(num)