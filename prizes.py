def mes(n):
    if(n==2):
        return 2
    if(n==1):
        return 1
    return n//2+1

n=int(input())
ans=mes(n)
l=[]
count=0
while(n!=1 and n!=2):
    l.append(ans)
    count+=1
    n=n-ans
    ans=mes(n)
l.append(ans)
count+=1 
print(count)
l.sort()
for i in l:
    print(i,end=' ')
