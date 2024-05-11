a=[2,6,3.2,9,'abc',1]
for i in a:
    if type(i)!=type(1):
        a.remove(i)
print(a)
