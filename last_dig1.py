n=int(input())
def fib(n):
    a=0
    b=1
    c=0
    if(n==1):
        c=1;
    for i in range(2,n+1):
        c=a%10+b%10
        a=b%10
        b=c%10
    return c
n=(n+2)%60
print((fib(n)-1)%10)
