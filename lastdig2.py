n=input().split()

def fib(n,fro):
    a=0;
    b=1;
    c=0;
    sum=0
    if(fro<=0):
        sum=0
    if(fro<=1 and n>=1):
        sum=1
    for i in range(2,n+1):
        c=a%10+b%10
        if(i >= fro):
            sum=sum%10+c%10
        a=b%10
        b=c%10
    return sum
a=int(n[1])
b=int(n[0])
a=a%60
b=b%60
if(a<b):
    a=a+60
print(fib(a,b)%10)
