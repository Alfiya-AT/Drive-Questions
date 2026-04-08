# 14. Find missing number from 1 to n. Input: [1,2,4,5], n=5

# def missing(l,n):
#     for i in range(1,n+1):
#         if i not in l:
#             return i
#     return -1

# using formuls 
# def missing(l,n):
#     s=(n*(n+1)//2)
#     return s-sum(l)

# Using XOR (Advanced 🔥)

def missing(l, n):
    xor_all = 0
    xor_arr = 0
    
    for i in range(1, n+1):
        xor_all ^= i
        
    for num in l:
        xor_arr ^= num
        
    return xor_all ^ xor_arr
l=[1,2,4,5] 
n=5
print(missing(l,n))