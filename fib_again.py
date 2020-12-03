n=input().split()
def pisanoPeriod(m):
    a = 0
    b = 1
    c = a + b
    for i in range(m*m):
        c = (a + b) % m
        a = b
        b = c
        if (a == 0 and b == 1):
            return i + 1
def fib(n,o):
    a=0;
    b=1;
    c=0;
    if(n==0):
        return a
    elif(n==1):
        return b
    else:
        for i in range(2,n+1):
            c=a%o+b%o
            a=b%o
            b=c%o
    return c
m=int(n[0])
o=int(n[1])
num=pisanoPeriod(o)
m=m%num
print(fib(m,o)%o)
