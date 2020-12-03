n=int(input())
s=input().split()
s1=input().split()
l=[]
l1=[]
for i in range(n):
    l.append(int(s[i]))
    l1.append(int(s1[i]))
l.sort()
l1.sort()
i=n-1
ans=0
while(i>=0):
    ans+=l[i]*l1[i]
    i-=1
print(ans)
