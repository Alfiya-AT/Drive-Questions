# 1. Reverse a string. Input: 'hello'

# Function                   O(n)
# rev = "".join(reversed(s))

# Slicing                    O(n)
# s[::-1]


def reverse(s):  
    
    
    # --stack----            O(n**2)
    # res=''
    # stack_s=list(s)
    # while stack_s:
    #     res+=stack_s.pop()
    # return res 


    #--2pointers---          Fast O(n)
    left=0
    right=len(s)-1
    list_s=list(s)
    while left<=right:
        list_s[left],list_s[right]=list_s[right],list_s[left]
        left+=1
        right-=1
    return "".join(list_s)


    # recursion              O(n**2)
    # if s=="":
    #     return s
    # return reverse(s[1:])+s[0]



s='hello'
print(reverse(s))
