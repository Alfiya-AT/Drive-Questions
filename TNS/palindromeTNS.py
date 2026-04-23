def palindrome(p):
    # 2. Check if a string is palindrome. Input: 'madam'
    # 2 ptr      T:O(n)         S:O(1)
    left=0
    right=len(p)-1
    while left<right:
        if p[left]!=p[right]:
            return False
        left+=1
        right-=1
    return True


    # ignoring space and case
    # p=p.upper()
    # p=p.replace(" ","")
    # same procedure 


p='madam ana'
print(palindrome(p))