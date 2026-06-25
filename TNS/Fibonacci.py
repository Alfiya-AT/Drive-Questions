# 8. Print Fibonacci series up to n terms. Input: n=6

# T:O(n) S:O(1)
# def Fibonacci(n):
#     a=0
#     b=1
#     if n<=0:
#         print("Inavalid input")
#     elif n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             a,b=b,a+b
#             print(b)


# T:O(n) S:O(n)
def Fibonacci(n):
    fib=[0,1]
    for i in range(2,n):
        fib.append(fib[-1]+fib[-2])
    print(fib)


n=6
Fibonacci(n)


# import math
# def fib(m):
#     phi = (1 + math.sqrt(5)) / 2
#     return int(round((phi**m) / math.sqrt(5)))

# for i in range(n):
#     print(fib(i))
