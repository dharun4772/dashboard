n=int(input())

def fib(n):
    sum=0
    a=0
    b=1
    c=0
    if(n>=1):
        sum=1;
    for i in range(2,n+1):
        c=a%10+b%10
        sum+=(c*c)%10
        a=b%10
        b=c%10
    return sum
n=n%60
print(fib(n)%10)
