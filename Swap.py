# 6. Swap two variables. Input: 
# tuple unpacking (a, b = b, a)  O(1)
# def Swap(a,b):
#     a,b=b,a
#     return a,b 


def Swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b 

a=5 
b=10
print(f"({a}, {b})")
print(Swap(a,b))