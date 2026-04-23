# 7. Find factorial of a number. Input: 5

# O(n) O(1)
def factorial(N):
    res=1
    i=1
    while i<=N:
        res*=i
        i+=1
    return res



# O(n)  O(n)
# def factorial(N):
#     if N==1 or N==0:
#         return 1
#     print(N)
#     return N*(factorial(N-1))

N=5


#using inbuild function  
# import math
# print(math.factorial(N)) 


print(factorial(N))