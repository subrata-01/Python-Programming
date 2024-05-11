n=int(input("enter number of elements : "))
a=[]
value=0
while 1<=n:
    j=2
    while j<value:
        if value%j==0:
            break
        j+=1
    if j==value:
        a.append(value)
        n-=1
    value+=1
print(a)
