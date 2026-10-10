# 11. Find second largest element. Input: [10, 20, 4, 45]


# best approach O(n) O(1)
def secondLargest(l):
    first=-float('inf')
    second=-float('inf')
    for i in l:
        if i>first:
            
            second=first
            first=i

        elif i>second and i!=first:
            second=i

    return second
    

# def secondLargest(l):
#     second=0
#     first=0
#     for i in l:
#         if i>first:
#             second=first
#             first=i
#     return second


# Heap
# import heapq
# def secondLargest(l):
#     return heapq.nlargest(2, set(l))[-1]


# using max fun 2 but here ur modifying the list 
# def secondLargest(l):
#     m=max(l)
#     l.remove(m)
#     return max(l)


l=[10, 20, 4, 45,98]
print(secondLargest(l))