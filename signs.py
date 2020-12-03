def minimum(l):
    li=[]
    for i in l:
        li.append(i[1])
    li.sort()
    return li[0]
    
n=int(input())
li=[]
l=[]
count=0
ans=[]
while(n):
    s=input().split()
    l.append([int(s[0]),int(s[1])])
    n-=1
while(len(l)):
    m=minimum(l)
    k=0
    flag=0
    while(k<len(l)):
        if(m<=l[k][1] and m>=l[k][0]):
            del l[k]
            flag=1
        else:
            k+=1
    if(flag==1):
        count+=1
        ans.append(m)
print(count)
for i in ans:
    print(i,end=' ')
