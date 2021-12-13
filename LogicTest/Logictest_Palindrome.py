def isPalindrome(input_str):
    input_str = input_str.upper()       # make them'all lowercase char
    return input_str == input_str[::-1] # [start:stop:step]

a = str(input("Test Sample :"))
result = isPalindrome(a)
if result: 
    print("palindrome")
else:
    print("not palindrome")
