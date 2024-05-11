a=[0,1]
n=int(input("enter number of elements : "))
i=0
while 2<=n:
    x=a[i]
    y=a[i+1]
    a.append(x+y)
    i+=1
    n-=1
print(a)
