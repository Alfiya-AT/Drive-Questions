# 12. Check if two strings are anagrams. Input: 'listen', 'silent'
# not correct approach 
# def anagrams(a,b):
    # d={}
    # for i in range(len(a)):
    #     d[a[i]]=d.get(a[i],b[i])

    # for j in a:   
    #     if j!=d.get(j):
    #         return False
    # return True

# def anagrams(a,b):
    # return sorted(a)==sorted(b)


# from collections import Counter 
# def anagrams(a,b):
#     return Counter(a)==Counter(b)

def anagrams(a,b):
    d={}
    if len(a)!=len(b):
        return False
    for i in a:
        d[i]=d.get(i,0)+1

    for j in b:
        if j not in d:
            return False
        d[j]-=1
        if d[j]==0:
            del d[j]
    return len(d)==0

a="listen"
b="silent"
print(anagrams(a,b))