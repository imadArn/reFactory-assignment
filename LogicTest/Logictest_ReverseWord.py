test_string = input('Input words :')
# "I am A Great human"

def split(s):
    split_str = s.split()    #splitting the word
    # print(split_str)
    length = len(split_str)
    # print(length)
    print(test_string)
    for ele in split_str:
        # print(len(ele))
        if len(ele)>1:
            ele_reverse = ele[::-1]
            if ele[0].isupper():
                print(ele_reverse.capitalize(), end=(' '))
            else:
                print(ele_reverse, end=' ')
        else:
            print(ele, end=(' '))    

#calling the func split
split(test_string) 
