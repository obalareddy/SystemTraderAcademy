'''Method  # 1
1) Find reverse of string
2) Check if reverse and original are same or not.'''

# function which return reverse of a string


def method1(s):
    ans = (s == s[::-1])

    if ans:
        print("Yes")
    else:
        print("No")


def method2(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            print("No")
            return
    print("Yes")
    return

#Method 3 : Method using inbuilt function to reverse a string

def method3(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        print("Yes")
    else:
        print("No")

# Driver code
s = input("Enter string: ")
method1(s)
method2(s)
method3(s)


