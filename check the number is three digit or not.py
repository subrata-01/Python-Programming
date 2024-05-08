n=int(input("enter a number : "))
count=0
while n>0:
    n=n//10
    count+=1
if count==3: 
    print("the number is three digits")
else:
    print("the number is not three digits")
