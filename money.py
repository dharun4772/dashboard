n=int(input())
l=[10,5,1]
count=0
for i in l:
    if(n>=i):
        count+=n//i
        n=n%i
print(count)
