# 9. Remove duplicates from list. Input: [1,2,2,3]

#T:O(n***2) S:O(n) 
# def duplicates(l):
#     res=[]
#     l.sort()
#     for i in range(len(l)):
#         if l[i] not in l[i+1:]:
#             res.append(l[i])
#     return res



#SET  O(n) O(n)  the order will get changed to sorted
# def duplicates(l):
#     l=set(l)
#     return list(l)


# 2ptr O(n log n) O(1)   it is only for sorted list 
# def duplicates(l):
#     i=0
#     j=1
#     while i<len(l) and j<len(l):
#         if l[i]!=l[j]:
#             i+=1
#             l[i]=l[j]
#             j+=1
#         j+=1
#     return l[:i+1]

# best approach 
def duplicates(l):
    res=[]
    seen=set()
    for i in l:
        if i not in seen:
            res.append(i)
            seen.add(i) 
    return res 


l=[1,2,2,3,3,3,4]
print(duplicates(l))