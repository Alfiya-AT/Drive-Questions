def fibo(n):
    term1=0
    term2=1
    res=[0]
    if n<=0:
        return "enter positive number"
    elif n==1:
        return term1
    else:
        for i in range(2,n+1):
            term3=term1+term2
            res.append(term2)
            term1=term2
            term2=term3
    return (res)
    

n=2
print(fibo(n))