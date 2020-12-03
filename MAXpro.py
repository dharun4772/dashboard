n=int(input())
s=input().split()
l=[]
for i in s:
    l.append(int(i))
l.sort()
sum=l[n-1]*l[n-2];
print(sum)
