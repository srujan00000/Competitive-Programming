#dynamic approach
def fibonacci(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

#recursion approach
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

#optimal approach
def fibonacci(n):
    a,b=0,1
    if n<0:
        print("incorrect input")
    elif n==0 or n==1:
        return n
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b