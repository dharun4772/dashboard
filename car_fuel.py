d=int(input())
m=int(input())
n=int(input())
l=[]
s=input().split()
for i in s:
    l.append(int(i))
l.append(d)
line=m
count=0
before,i=0,0
while(i<len(l)):
    if(l[i]<=line):
        before=l[i]
        d=l[i]
        i+=1
    else:
        if(line==m+before):
            count=-1
            break
        line=m+before
        count+=1
print(count)
