# 4. Check if a number is even or odd. Input: 7

# Using bitwise function   fastest low level   T:O(1)   in bitwise if last digit is 0 then its even else odd
def EvenOdd(n):
    if n&1==0:
        return "Even" 
    return "Odd"


# using formula res=(n//2)*n if res==n then even    T:O(1)
# def EvenOdd(n):
#     res=(n//2)*2
#     if res==n:
#         return "Even"
#     return "Odd"


# using mod operator O(1)

# def EvenOdd(n):
#     if n%2==0:
#         return "Even"   
#     return "Odd"


# using dictonary 
# def EvenOdd(n):
#     return {0: "Even", 1: "Odd"}[n % 2]



n=7
print(EvenOdd(n))