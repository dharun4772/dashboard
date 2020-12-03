n=int(input())
j=1
while(j<=n):
    length=int(input())
    s=input().split()
    l=[]
    for i in range(length):
        l.append(int(s[i]))
    i,count=1,1
    high=[]
    change=l[0]-l[i]
    while(i<length-1):
        if(change==l[i]-l[i+1]):
            count+=1
        else:
            high.append(count)
            count=1
            change=l[i]-l[i+1]
        i+=1
    high.append(count)
    high.sort()
    print("Case #{}: {}".format(j,high[len(high)-1]+1))
    j+=1
