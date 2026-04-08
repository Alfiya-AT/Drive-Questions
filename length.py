# 10. Find length of string without using len(). Input: 'hello'

# O(n)  O(n)   best 
# def length(n):
#     l=0
#     for i in n:
#         l+=1
#     return l


def length(n):
    count=0
    while True:
        try :
            n[count]
            count+=1
        except IndexError:
            return count


#recursion take extra space O(n)  O(n)
# def length(s):
#     if s == "":
#         return 0
#     return 1 + length(s[1:])


n='hello'
print(length(n))