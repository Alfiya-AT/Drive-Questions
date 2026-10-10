# 5. Count vowels in a string. Input: 'hello world'   

# T: O(n)  S:O(1)
# def vowels(s):
#     cnt=0
#     v=['a','e','i','o','u']
#     for i in s:
#         if i.lower() in v:
#             cnt+=1
#     return cnt

def vowels(s):
    return sum(1 for i in s if i in 'aeiou')

s='hello world'
print(vowels(s))