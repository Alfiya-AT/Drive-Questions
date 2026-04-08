# 3. Find the largest element in a list. Input: [1, 5, 3, 9]


def largestElement(l):

# using loop traversel T:O(n)
    largest=l[0]
    for i in range(1,len(l)):
        if l[i]>largest:
            largest=l[i]
    return largest


# using sort T: O(nlogn)
    # l.sort()
    # return l[-1]

#using max  T:O(n)
    # return max(l)



# using heap T: O(nLogk)=> O(n)
# import heapq

# def largestElement(l):
#     return heapq.nlargest(1, l)[0]

l=[1, 5, 3, 9]
print(largestElement(l))