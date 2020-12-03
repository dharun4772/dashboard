s=input().split()
a=int(s[0])
b=int(s[1])
def gcd(a,b):
    while(b!=0):
        if(a<b):
            t=a
            a=b
            b=t
        else:
            rem=a%b
            a=b
            b=rem
    return a
ans=(a*b)//gcd(a,b);
print(ans)
